/* ===== EMOO — Smart Assistant ===== */

const API_URL = '/chat';

const sidebar = document.getElementById('sidebar');
const sidebarOverlay = document.getElementById('sidebarOverlay');
const menuBtn = document.getElementById('menuBtn');
const messagesEl = document.getElementById('messages');
const messageInput = document.getElementById('messageInput');
const sendBtn = document.getElementById('sendBtn');
const thinkingEl = document.getElementById('thinking');
const liveTime = document.getElementById('liveTime');
const liveDate = document.getElementById('liveDate');
const emojiBtn = document.getElementById('emojiBtn');
const emojiPicker = document.getElementById('emojiPicker');
const toast = document.getElementById('toast');
const historyList = document.getElementById('historyList');
const clearHistoryBtn = document.getElementById('clearHistoryBtn');
const attachBtn = document.getElementById('attachBtn');
const imageInput = document.getElementById('imageInput');
const shiningOverlay = document.getElementById('shiningOverlay');

const MAX_IMAGE_SIZE = 5 * 1024 * 1024;

const panelMap = {
  chat: 'viewChat',
  history: 'viewHistory',
  study: 'viewStudy',
  delete: 'viewDelete',
  settings: 'viewSettings',
  theme: 'viewTheme',
  about: 'viewAbout',
};

const CREATOR_PATTERNS = [
  /who (made|created|built|developed|designed) emoo/i,
  /who is (the )?(creator|developer|maker|owner) of emoo/i,
  /emoo (ko|ke) kis(ne)? (ne )?(banaya|bnaya|bana|create)/i,
  /kis ny emoo/i,
  /kisne emoo/i,
  /emoo kis ne banaya/i,
  /who owns emoo/i,
  /made by whom/i,
  /creator of emoo/i,
];

const CREATOR_REPLY =
  'EMOO was lovingly created by Sehrish Malik 💕\n\n' +
  'She is an intelligent, creative, and wonderfully innocent soul who poured her heart into building me. ' +
  'Sehrish combines smart engineering with a gentle, caring spirit — and that is exactly why EMOO feels so warm, helpful, and professional! ✨\n\n' +
  'I am proud to be her creation. Whenever you use EMOO, you are experiencing the vision of Sehrish Malik 💜';

let chatHistory = JSON.parse(localStorage.getItem('emoo_history') || '[]');
let savedMessages = JSON.parse(localStorage.getItem('emoo_saved') || '[]');
let isWaiting = false;

/* ===== SETTINGS ===== */
const settings = {
  sound: localStorage.getItem('emoo_sound') !== 'false',
  autoSave: localStorage.getItem('emoo_autosave') === 'true',
  timestamps: localStorage.getItem('emoo_timestamps') !== 'false',
  typing: localStorage.getItem('emoo_typing') !== 'false',
  compact: localStorage.getItem('emoo_compact') === 'true',
  notify: localStorage.getItem('emoo_notify') === 'true',
  fontSize: localStorage.getItem('emoo_fontsize') || 'medium',
  enterSend: localStorage.getItem('emoo_entersend') !== 'false',
  theme: localStorage.getItem('emoo_theme') || 'pink',
};

function playSound(type = 'send') {
  if (!settings.sound) return;
  try {
    const ctx = new (window.AudioContext || window.webkitAudioContext)();
    const osc = ctx.createOscillator();
    const gain = ctx.createGain();
    osc.connect(gain);
    gain.connect(ctx.destination);
    osc.frequency.value = type === 'send' ? 520 : 380;
    gain.gain.setValueAtTime(0.08, ctx.currentTime);
    gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + 0.15);
    osc.start(ctx.currentTime);
    osc.stop(ctx.currentTime + 0.15);
  } catch (_) { /* silent */ }
}

function applySettings() {
  document.getElementById('soundToggle').checked = settings.sound;
  document.getElementById('autoSaveToggle').checked = settings.autoSave;
  document.getElementById('timestampToggle').checked = settings.timestamps;
  document.getElementById('typingToggle').checked = settings.typing;
  document.getElementById('compactToggle').checked = settings.compact;
  document.getElementById('notifyToggle').checked = settings.notify;
  document.getElementById('fontSizeSelect').value = settings.fontSize;
  document.getElementById('enterSendToggle').checked = settings.enterSend;

  messagesEl.classList.toggle('compact', settings.compact);
  messagesEl.classList.remove('font-small', 'font-large');
  if (settings.fontSize === 'small') messagesEl.classList.add('font-small');
  if (settings.fontSize === 'large') messagesEl.classList.add('font-large');

  document.querySelectorAll('.msg-time').forEach((el) => {
    el.classList.toggle('hidden', !settings.timestamps);
  });
}

function saveSetting(key, value) {
  settings[key] = value;
  const map = {
    sound: 'emoo_sound',
    autoSave: 'emoo_autosave',
    timestamps: 'emoo_timestamps',
    typing: 'emoo_typing',
    compact: 'emoo_compact',
    notify: 'emoo_notify',
    fontSize: 'emoo_fontsize',
    enterSend: 'emoo_entersend',
    theme: 'emoo_theme',
  };
  localStorage.setItem(map[key], String(value));
  applySettings();
}

/* ===== THEME ===== */
function applyTheme(themeName) {
  document.body.className = themeName === 'pink' ? 'theme-pink' : `theme-${themeName}`;
  
  // Add shining miraculous effect
  document.body.classList.add('shining-active');
  
  document.querySelectorAll('.theme-btn').forEach((b) => {
    b.classList.toggle('active', b.dataset.theme === themeName);
  });
  
  settings.theme = themeName;
  localStorage.setItem('emoo_theme', themeName);
  
  // Update bubble colors
  updateBubbleColors(themeName);
}

function updateBubbleColors(theme) {
  const colors = {
    pink: '#ff69b4',
    purple: '#7B1FA2',
    mint: '#5ecfb0',
    maroon: '#c44d6a',
    black: '#4a4a8a'
  };
  const color = colors[theme] || '#ff69b4';
  document.querySelectorAll('.bubble').forEach(b => {
    b.style.background = `radial-gradient(circle at 30% 30%, rgba(255,255,255,0.55), ${color}40)`;
  });
}

/* ===== CLOCK ===== */
function updateClock() {
  const now = new Date();
  liveTime.textContent = now.toLocaleTimeString('en-US', {
    hour: '2-digit', minute: '2-digit', second: '2-digit', hour12: true,
  });
  liveDate.textContent = now.toLocaleDateString('en-GB', {
    day: 'numeric', month: 'long', year: 'numeric', weekday: 'long',
  });
}
updateClock();
setInterval(updateClock, 1000);

/* ===== SIDEBAR ===== */
function openSidebar() {
  sidebar.classList.add('open');
  sidebarOverlay.classList.add('show');
}
function closeSidebar() {
  sidebar.classList.remove('open');
  sidebarOverlay.classList.remove('show');
}

menuBtn.addEventListener('click', () => {
  if (sidebar.classList.contains('open')) closeSidebar();
  else openSidebar();
});
sidebarOverlay.addEventListener('click', closeSidebar);

/* ===== NAVIGATION ===== */
document.querySelectorAll('.nav-item').forEach((btn) => {
  btn.addEventListener('click', () => {
    switchPanel(btn.dataset.panel);
    document.querySelectorAll('.nav-item').forEach((b) => b.classList.remove('active'));
    btn.classList.add('active');
    closeSidebar();
  });
});

function switchPanel(name) {
  Object.values(panelMap).forEach((id) => {
    document.getElementById(id).classList.remove('active');
  });
  const viewId = panelMap[name];
  if (viewId) document.getElementById(viewId).classList.add('active');
  if (name === 'history') renderHistoryList();
}

function activateNav(panel) {
  document.querySelectorAll('.nav-item').forEach((b) => b.classList.remove('active'));
  const btn = document.querySelector(`[data-panel="${panel}"]`);
  if (btn) btn.classList.add('active');
}

/* ===== TOAST ===== */
function showToast(msg) {
  toast.textContent = msg;
  toast.classList.add('show');
  toast.classList.remove('hidden');
  setTimeout(() => toast.classList.remove('show'), 2600);
}

/* ===== UTILS ===== */
function formatTime(date = new Date()) {
  return date.toLocaleTimeString('en-US', { hour: '2-digit', minute: '2-digit', hour12: true });
}

function escapeHtml(str) {
  const d = document.createElement('div');
  d.textContent = str;
  return d.innerHTML;
}

function escapeAttr(str) {
  return str.replace(/"/g, '&quot;').replace(/'/g, '&#39;');
}

function scrollToBottom() {
  messagesEl.scrollTop = messagesEl.scrollHeight;
}

function isCreatorQuestion(text) {
  return CREATOR_PATTERNS.some((p) => p.test(text));
}

function showThinking(show) {
  if (!settings.typing) {
    thinkingEl.classList.add('hidden');
    return;
  }
  thinkingEl.classList.toggle('hidden', !show);
}

/* ===== MESSAGES ===== */
function addImageMessage(imageSrc, caption = '') {
  const row = document.createElement('div');
  row.className = 'msg-row user';
  const captionHtml = caption ? `<p class="msg-caption">${escapeHtml(caption)}</p>` : '';
  const timeClass = settings.timestamps ? '' : ' hidden';

  row.innerHTML = `
    <div class="bubble-wrap">
      <div class="msg-bubble user-bubble">
        <img class="msg-image" src="${imageSrc}" alt="Uploaded picture" />
        ${captionHtml}
        <div class="msg-meta">
          <span class="msg-time${timeClass}">${formatTime()}</span>
          <span class="read-check">✓✓</span>
        </div>
      </div>
    </div>`;

  messagesEl.appendChild(row);
  scrollToBottom();
  return row;
}

function addMessage(text, type = 'ai', saveable = true) {
  const row = document.createElement('div');
  row.className = `msg-row ${type}`;
  const timeClass = settings.timestamps ? '' : ' hidden';
  const formatted = escapeHtml(text).replace(/\n/g, '<br>');

  if (type === 'ai') {
    row.innerHTML = `
      <div class="msg-avatar"><img src="emoo.png" alt="EMOO" /></div>
      <div class="bubble-wrap">
        <div class="msg-bubble ai-bubble">
          <p>${formatted}</p>
          <div class="msg-meta">
            <span class="msg-time${timeClass}">${formatTime()}</span>
            ${saveable ? `<button class="save-btn" title="Save message" data-msg="${escapeAttr(text)}">🔖</button>` : ''}
          </div>
        </div>
      </div>`;
  } else {
    row.innerHTML = `
      <div class="bubble-wrap">
        <div class="msg-bubble user-bubble">
          <p>${formatted}</p>
          <div class="msg-meta">
            <span class="msg-time${timeClass}">${formatTime()}</span>
            <span class="read-check">✓✓</span>
          </div>
        </div>
      </div>`;
  }

  messagesEl.appendChild(row);
  scrollToBottom();

  if (saveable && type === 'ai') {
    const saveBtnEl = row.querySelector('.save-btn');
    if (saveBtnEl) saveBtnEl.addEventListener('click', () => saveMessage(text, saveBtnEl));
  }

  if (settings.notify && type === 'ai' && 'Notification' in window && Notification.permission === 'granted') {
    new Notification('EMOO replied 💜', { body: text.slice(0, 80), icon: 'emoo.png' });
  }

  return row;
}

function saveMessage(text, btnEl) {
  if (savedMessages.includes(text)) {
    showToast('Already saved! 💜');
    return;
  }
  savedMessages.push(text);
  localStorage.setItem('emoo_saved', JSON.stringify(savedMessages));
  btnEl.classList.add('saved');
  btnEl.textContent = '✅';
  showToast('Message saved! 🔖');
  playSound('save');
}

document.querySelectorAll('.save-btn').forEach((btn) => {
  btn.addEventListener('click', () => saveMessage(btn.dataset.msg, btn));
});

/* ===== SEND ===== */
async function sendMessage() {
  const text = messageInput.value.trim();
  if (!text || isWaiting) return;

  addMessage(text, 'user');
  messageInput.value = '';
  playSound('send');
  chatHistory.push({ role: 'user', content: text, time: new Date().toISOString() });
  saveChatHistory();

  isWaiting = true;
  showThinking(true);
  scrollToBottom();

  if (isCreatorQuestion(text)) {
    await delay(800);
    showThinking(false);
    addMessage(CREATOR_REPLY, 'ai');
    chatHistory.push({ role: 'ai', content: CREATOR_REPLY, time: new Date().toISOString() });
    saveChatHistory();
    isWaiting = false;
    return;
  }

  try {
    const reply = await fetchAIReply(text);
    showThinking(false);
    addMessage(reply, 'ai');
    chatHistory.push({ role: 'ai', content: reply, time: new Date().toISOString() });
    saveChatHistory();

    if (settings.autoSave) {
      savedMessages.push(reply);
      localStorage.setItem('emoo_saved', JSON.stringify(savedMessages));
    }
  } catch (err) {
    showThinking(false);
    addMessage('Oops! Something went wrong 💔 Please check if app.py is running.', 'ai', false);
    console.error(err);
  }

  isWaiting = false;
}

function delay(ms) {
  return new Promise((r) => setTimeout(r, ms));
}

/* ===== API CALL ===== */
async function fetchAIReply(message, imagePayload = null) {
  const body = { message };
  if (imagePayload) {
    body.image = imagePayload.base64;
    body.mime_type = imagePayload.mimeType;
  }

  const res = await fetch(API_URL, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(body),
  });

  if (!res.ok) throw new Error('API error');
  const data = await res.json();
  return data.reply || data.response || data.message || 'No reply received.';
}

function readImageFile(file) {
  return new Promise((resolve, reject) => {
    const reader = new FileReader();
    reader.onload = () => resolve(reader.result);
    reader.onerror = () => reject(new Error('Could not read image'));
    reader.readAsDataURL(file);
  });
}

async function sendImageMessage(file) {
  if (!file || isWaiting) return;

  if (!file.type.startsWith('image/')) {
    showToast('Please choose a picture file 🖼️');
    return;
  }
  if (file.size > MAX_IMAGE_SIZE) {
    showToast('Picture is too large (max 5 MB) 📎');
    return;
  }

  const caption = messageInput.value.trim();
  const dataUrl = await readImageFile(file);
  const base64 = dataUrl.split(',')[1];

  addImageMessage(dataUrl, caption);
  messageInput.value = '';
  imageInput.value = '';
  playSound('send');

  const historyLabel = caption || `[Picture: ${file.name}]`;
  chatHistory.push({ role: 'user', content: historyLabel, time: new Date().toISOString() });
  saveChatHistory();

  isWaiting = true;
  showThinking(true);
  scrollToBottom();

  try {
    const prompt = caption || 'What is in this image? Please describe it and help me.';
    const reply = await fetchAIReply(prompt, { base64, mimeType: file.type });
    showThinking(false);
    addMessage(reply, 'ai');
    chatHistory.push({ role: 'ai', content: reply, time: new Date().toISOString() });
    saveChatHistory();
    if (settings.autoSave) {
      savedMessages.push(reply);
      localStorage.setItem('emoo_saved', JSON.stringify(savedMessages));
    }
  } catch (err) {
    showThinking(false);
    addMessage('Oops! Could not read your picture 💔 Please check if app.py is running.', 'ai', false);
    console.error(err);
  }

  isWaiting = false;
}

sendBtn.addEventListener('click', sendMessage);
messageInput.addEventListener('keydown', (e) => {
  if (e.key === 'Enter' && !e.shiftKey && settings.enterSend) {
    e.preventDefault();
    sendMessage();
  }
});

/* ===== EMOJI ===== */
emojiBtn.addEventListener('click', (e) => {
  e.stopPropagation();
  emojiPicker.classList.toggle('hidden');
});

emojiPicker.querySelectorAll('button').forEach((btn) => {
  btn.addEventListener('click', () => {
    messageInput.value += btn.textContent;
    messageInput.focus();
    emojiPicker.classList.add('hidden');
  });
});

document.addEventListener('click', (e) => {
  if (!emojiPicker.contains(e.target) && e.target !== emojiBtn) {
    emojiPicker.classList.add('hidden');
  }
});

/* ===== HISTORY ===== */
function saveChatHistory() {
  localStorage.setItem('emoo_history', JSON.stringify(chatHistory));
}

function renderHistoryList() {
  historyList.innerHTML = '';
  const items = chatHistory.filter((m) => m.role === 'user').slice(-25).reverse();

  if (items.length === 0) {
    historyList.innerHTML = '<li>No history yet 💜</li>';
    return;
  }

  items.forEach((item) => {
    const li = document.createElement('li');
    li.textContent = item.content.slice(0, 70) + (item.content.length > 70 ? '...' : '');
    li.addEventListener('click', () => {
      switchPanel('chat');
      activateNav('chat');
      messageInput.value = item.content.startsWith('[Picture:') ? '' : item.content;
      messageInput.focus();
    });
    historyList.appendChild(li);
  });
}

clearHistoryBtn.addEventListener('click', () => {
  chatHistory = [];
  savedMessages = [];
  localStorage.removeItem('emoo_history');
  localStorage.removeItem('emoo_saved');
  messagesEl.innerHTML = '';
  addMessage("Hi! I'm EMOO 💜 Your smart & friendly assistant. How can I help you today? ✨", 'ai');
  showToast('History cleared! 🗑️');
  renderHistoryList();
});

/* ===== STUDY ===== */
document.querySelectorAll('.chip').forEach((chip) => {
  chip.addEventListener('click', () => {
    switchPanel('chat');
    activateNav('chat');

    const greeting = chip.dataset.greeting;
    if (greeting) addMessage(greeting, 'ai', false);

    messageInput.value = chip.dataset.prompt;
    messageInput.focus();
    showToast('Topic ready — press Send! 📚');
  });
});

/* ===== SETTINGS BINDINGS ===== */
document.getElementById('soundToggle').addEventListener('change', (e) => saveSetting('sound', e.target.checked));
document.getElementById('autoSaveToggle').addEventListener('change', (e) => saveSetting('autoSave', e.target.checked));
document.getElementById('timestampToggle').addEventListener('change', (e) => saveSetting('timestamps', e.target.checked));
document.getElementById('typingToggle').addEventListener('change', (e) => saveSetting('typing', e.target.checked));
document.getElementById('compactToggle').addEventListener('change', (e) => saveSetting('compact', e.target.checked));
document.getElementById('enterSendToggle').addEventListener('change', (e) => saveSetting('enterSend', e.target.checked));
document.getElementById('fontSizeSelect').addEventListener('change', (e) => saveSetting('fontSize', e.target.value));
document.getElementById('notifyToggle').addEventListener('change', (e) => {
  if (e.target.checked && 'Notification' in window) {
    Notification.requestPermission().then((perm) => {
      if (perm !== 'granted') {
        e.target.checked = false;
        showToast('Notifications blocked by browser 🔔');
      } else {
        saveSetting('notify', true);
        showToast('Notifications enabled! 🔔');
      }
    });
  } else {
    saveSetting('notify', e.target.checked);
  }
});

/* ===== THEME BTNS ===== */
document.querySelectorAll('.theme-btn').forEach((btn) => {
  btn.addEventListener('click', () => {
    applyTheme(btn.dataset.theme);
    showToast(`✨ Theme: ${btn.textContent.trim()} with Shining Miraculous ✨`);
  });
});

/* ===== TOP BAR ===== */
document.getElementById('searchBtn').addEventListener('click', () => {
  switchPanel('chat');
  activateNav('chat');
  messageInput.focus();
  showToast('Type to search in chat 🔍');
});
document.getElementById('notifyBtn').addEventListener('click', () => {
  switchPanel('settings');
  activateNav('settings');
  showToast('Enable notifications in Settings 🔔');
});
document.getElementById('moreBtn').addEventListener('click', () => {
  switchPanel('settings');
  activateNav('settings');
});

/* ===== IMAGE UPLOAD ===== */
attachBtn.addEventListener('click', () => imageInput.click());
imageInput.addEventListener('change', () => {
  const file = imageInput.files?.[0];
  if (file) sendImageMessage(file);
});

/* ===== INIT ===== */
applySettings();
applyTheme(settings.theme);