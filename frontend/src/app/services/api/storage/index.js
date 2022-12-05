class JSONStorage {
  constructor(storage) {
    if (!storage || typeof storage !== 'object') throw new Error(`Expected a Storage object, got ${storage}`);
    this.storage = storage;
  }

  set(k, v) {
    const value = JSON.stringify(v);
    if (typeof value === 'undefined') {
      this.storage.removeItem(k);
      return;
    }

    this.storage.setItem(k, value);
  }

  get(k) {
    const str = this.storage.getItem(k);
    if (str === null) return undefined;

    return JSON.parse(str);
  }

  remove(k) {
    this.storage.removeItem(k);
  }
}

const storage = new JSONStorage(window.localStorage);

export default storage;
