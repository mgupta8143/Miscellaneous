"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.deactivate = exports.activate = void 0;
const vscode = require("vscode");
// your extension is activated the very first time the command is executed
function activate(context) {
    context.subscriptions.push(vscode.commands.registerCommand('tutorialtime.start', () => {
        const panel = vscode.window.createWebviewPanel('tutorialtime', 'Tutorial', vscode.ViewColumn.One, { enableScripts: true });
        panel.webview.html = getWebviewContent();
    }));
}
exports.activate = activate;
function getWebviewContent() {
    return `<!DOCTYPE html>
			<html lang="en">
				<head>
					<meta charset="UTF-8">
					<meta name="viewport" content="width=device-width, initial-scale=1.0">
					<title>Cat Coding</title>
				</head>
				<body
				<h1>Hello</h1>
				<iframe width="1280" height="720" 
						src="https://www.youtube.com/embed/dQw4w9WgXcQ?rel=0&amp;showinfo=0"
						frameborder="0" allowfullscreen>
				</iframe>
					
				</body>
			</html>`;
}
// this method is called when your extension is deactivated
function deactivate() { }
exports.deactivate = deactivate;
//# sourceMappingURL=extension.js.map