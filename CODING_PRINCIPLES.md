# 💻📝 Coding and Documentation Principles

> **These principles apply to both code AND documentation.** Whether you're writing JavaScript functions or markdown guides, these ADHD-friendly principles help create clear, maintainable, and accessible content that respects how our brains work.

## Core Philosophy
**ADHD-Friendly • DRY • Modular • KISS • MVP-First • Pragmatic OOP • Progressive Enhancement • Single Source of Truth**

## 🧠 ADHD-Friendly Development
- **Clear file names** that describe purpose immediately
- **One file, one purpose** - avoid cognitive overload
- **Descriptive variable names** over clever abbreviations
- **Visual separators** in code (clear sections, spacing)
- **TODO comments** for context switching
- **Immediate feedback** - console logs, progress indicators

```javascript
// ✅ GOOD - Clear intent
const downloadPhotosForChild = async (childName) => {
  console.log(`📸 Starting download for ${childName}...`);
  // ... code
}

// ❌ BAD - Unclear abbreviation
const dlPics = async (cn) => {
  // ... code
}
```

## 🔁 DRY (Don't Repeat Yourself)
- **Extract common patterns** into functions/modules
- **Configuration over duplication**
- **Shared constants** in single location

```python
# ✅ GOOD - Single source for selectors
SELECTORS = {
    'photo_modal': '[data-testid="photo-modal"]',
    'download_btn': '[data-testid="download-button"]',
    'next_btn': '[data-testid="next-photo"]'
}

# ❌ BAD - Repeated strings everywhere
driver.find_element(By.CSS_SELECTOR, '[data-testid="photo-modal"]')
# ... later in code
element = driver.find_element(By.CSS_SELECTOR, '[data-testid="photo-modal"]')
```

## 📦 Modular Architecture
- **Small, focused modules** doing one thing well
- **Clear interfaces** between modules
- **Dependency injection** when needed

```javascript
// ✅ GOOD - Modular structure
// dateUtils.js
export const formatDate = (date) => { /* ... */ }
export const parseEstonianDate = (dateStr) => { /* ... */ }

// photoDownloader.js
import { formatDate } from './dateUtils.js';

// ❌ BAD - Everything in one file
function downloadPhotos() {
  // Date parsing logic mixed with download logic
  // UI updates mixed with business logic
}
```

## 🎯 KISS (Keep It Simple, Stupid)
- **Start simple**, add complexity only when needed
- **Obvious code** > clever code
- **Flat is better** than nested

```python
# ✅ GOOD - Simple and clear
def is_photo_downloaded(filename):
    return os.path.exists(f"downloads/{filename}")

# ❌ BAD - Over-engineered
class PhotoExistenceVerificationManager:
    def __init__(self, strategy_factory):
        self.verification_strategy = strategy_factory.create()
    
    def verify_existence_status(self, photo_identifier):
        return self.verification_strategy.execute_verification(photo_identifier)
```

## 🚀 MVP-First Approach
- **Working solution first**, optimization later
- **Manual process** before automation
- **Hardcoded values** before configuration
- **Console script** before GUI

```javascript
// Phase 1: MVP - Hardcoded, works for one use case
const downloadPhotos = () => {
  const photos = document.querySelectorAll('.photo');
  photos.forEach(photo => photo.click());
}

// Phase 2: Enhancement - Add configuration
const downloadPhotos = (options = {}) => {
  const selector = options.selector || '.photo';
  const delay = options.delay || 1000;
  // ... enhanced version
}
```

## 🏗️ Pragmatic OOP
- **Use classes when** modeling real-world entities
- **Use functions when** performing transformations
- **Avoid inheritance hell** - prefer composition

```python
# ✅ GOOD - OOP where it makes sense
class PhotoDownloader:
    def __init__(self, child_name, date_range):
        self.child_name = child_name
        self.date_range = date_range
        self.downloaded_count = 0
    
    def download(self):
        # ... download logic

# ✅ ALSO GOOD - Simple function for simple task
def format_filename(date, index):
    return f"photo_{date}_{index:03d}.jpg"

# ❌ BAD - OOP for everything
class FilenameFormatterFactory:
    def create_formatter(self):
        return FilenameFormatter()
```

## 📈 Progressive Enhancement
- **Make it work** ✓
- **Make it right** ✓
- **Make it fast** (only if needed)

```javascript
// Version 1: Works
photos.forEach(photo => {
  downloadPhoto(photo);
});

// Version 2: Better error handling
for (const photo of photos) {
  try {
    await downloadPhoto(photo);
  } catch (error) {
    console.error(`Failed: ${photo.id}`, error);
  }
}

// Version 3: Performance optimization (only if needed)
await Promise.all(
  photos.map(photo => 
    downloadWithRetry(photo, { maxRetries: 3 })
  )
);
```

## 🎯 Single Source of Truth
- **One config file** for all settings
- **One place** for each piece of business logic
- **Centralized state** management
- **IMPORTANT:** This applies to DOCUMENTATION too!
  - Don't duplicate guidelines across multiple files
  - Reference other documents instead of repeating
  - Keep one authoritative source for each concept
  - Example: AI response format rules → AI_COLLABORATION_GUIDE.md

```javascript
// config.js - Single source for all configuration
export const CONFIG = {
  api: {
    baseUrl: 'https://eliis.eu',
    timeout: 30000
  },
  download: {
    batchSize: 10,
    retryAttempts: 3
  },
  paths: {
    downloads: './downloads',
    logs: './logs'
  }
};

// ❌ BAD - Configuration scattered
// file1.js
const API_URL = 'https://eliis.eu';
// file2.js
const BASE_URL = 'https://eliis.eu';
// file3.js
const ELIIS_URL = 'https://eliis.eu';
```

## 📝 Practical Examples

### JavaScript/Browser
```javascript
// Simple, ADHD-friendly photo downloader
const downloadPhotosForMonth = async (monthYear) => {
  console.log(`\n📅 Starting download for ${monthYear}\n`);
  
  const photos = await findPhotosForMonth(monthYear);
  console.log(`📸 Found ${photos.length} photos\n`);
  
  for (const [index, photo] of photos.entries()) {
    console.log(`⬇️  Downloading ${index + 1}/${photos.length}...`);
    
    try {
      await downloadPhoto(photo);
      console.log(`✅ Success!`);
    } catch (error) {
      console.log(`❌ Failed: ${error.message}`);
    }
  }
  
  console.log(`\n✨ Done! Downloaded photos for ${monthYear}\n`);
};
```

### Python
```python
# Clear, modular structure
class PhotoDownloadSession:
    """Simple session manager for downloading photos"""
    
    def __init__(self, child_name: str):
        self.child_name = child_name
        self.downloaded = []
        self.failed = []
    
    def download_date_range(self, start_date: str, end_date: str):
        """Download photos for a date range"""
        print(f"\n📅 Downloading photos for {self.child_name}")
        print(f"📆 Period: {start_date} to {end_date}\n")
        
        dates = self._get_dates_in_range(start_date, end_date)
        
        for date in dates:
            self._download_photos_for_date(date)
        
        self._print_summary()
    
    def _download_photos_for_date(self, date: str):
        """Download all photos for a specific date"""
        # Simple, focused method doing one thing
        pass
```

## 🚨 Anti-Patterns to Avoid
```javascript
// ❌ Callback hell
getData(function(a) {
  getMoreData(a, function(b) {
    getMoreData(b, function(c) {
      getMoreData(c, function(d) {
        // ... nightmare
      });
    });
  });
});

// ❌ Premature optimization
const PhotoCache = new WeakMap();
const MemoizedPhotoFactory = (() => {
  // ... 200 lines of caching logic for 10 photos
})();

// ❌ Over-abstraction
class AbstractPhotoDownloaderFactoryInterface {
  // ... why?
}
```

## 🚨 Critical Error Handling
- **NO SILENT FAILURES** - Always make errors visible to users. Never fail silently or hide problems. Users must know immediately when something isn't working so they can make informed decisions.

## 🤖 AI Collaboration Guidelines
- **Step-by-step implementation** - Present one method/function at a time for approval. Get explicit approval before writing code. Build incrementally rather than large chunks.
- **Question complexity first** - Challenge initial estimates and assumptions. Simple solutions often work better than elaborate ones. Trust domain expertise over theoretical complexity.

## 👥 User Experience Principles  
- **User-visible error states** - Extensions should show clear status (working/failed/stuck). Never leave users guessing if something is broken. Progress indicators should reflect real progress, not fake timers.

## 🎯 Remember
- **Working code** > Perfect code
- **Clear code** > Clever code
- **Today's solution** > Tomorrow's perfection
- **Ship it** > Endless refactoring