const { app, BrowserWindow } = require("electron");

const createWindow = () => {
    const win = new BrowserWindow({
        width: 1024,
        height: 576,
        autoHideMenuBar: true,
    });
    win.loadFile("index.html");
}

app.whenReady().then(() => {
    createWindow();
});

app.on('window-all-closed', () => {app.quit()})