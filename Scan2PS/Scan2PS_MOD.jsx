/**
 *  Photoshop Script to control the Scan2Net Scanners
 *
 * @file: Scan2PS.jsx
 * @author: Florian Roemer
 */

var PORT = 2000,
	HTTP_PORT = 80,
	IMAGE_TIMEOUT = 240, 
	TIMEOUT = 2,
	IMAGE_FUNCTION = "image",
	CONN_ERR = "error",
	CGI_GET = "GET /cgi/",
	CGI_PARAM_START = "?",
	CGI_PARAM_CONTINUE = "+",
	IMG_ENCODING = "binary",
	DEVICE_PATH = "C:\\\\",
	IMG_FILENAME = "scan",
	JPEG_FORMAT = "jpeg",
	JPEG_FILE_ENDING = "jpg",
	TIFF = "tiff",
	HISTORY_SAVE_FILE = "/scan2shop_IP.txt",
	HISTORY_SEPERATOR = ";",
	HISTORY_ENTRY_SEPERATOR = "_",
	WIZARD = "/ScanWizard.html",
	WIN = "Windows",
	IMG_BLOCK_SIZE = 1024*1024*100,
	LOAD_BAR_STEPS = 4;

var main = {
	close : false,
	scanned : false,
	loadClose : false,
	stopBtnFlag : false,
	
	win : "",
	loadWin : "",
	lblConnStatus: "",
	lblIp : "",
	inIpAddr : "",	
	lbLast : "",
	drpLast : "",	
	btnClear : "",
	btnConn : "",
	rdJpeg : "",
	rdTiff : "",
	btnScan : "",
	btnStop : "",
	btnRe : "",
	btnOpenWizard : "",
	hisArr : [],
	prog : "",
	lbProg : "",
	btnHelp : "",
	btnClose : "",

	init : function () {		
		main.hisArr =  main.getData();		
		main.createWindow();
		main.selHis();
		main.close = false;

		// ------------------------------Just for testing----------------------------------------
		/*conn.ip = "192.168.61.225:80";
		conn.encoding = "binary";
		
		$.writeln(conn.ip);
		$.writeln(conn.encoding);
		$.writeln(conn.callApi("s2ninfo", null, false, false, false));
		conn.sessionId = (conn.callApi("s2nopen", null, false, false, false)).split("ID: ")[1];
	
		$.writeln("sessionID: " + conn.sessionId);
	
		$.writeln(conn.callApi("set", "fileformat:" + main.getFormat(false), true, false, false));
		$.writeln(conn.callApi("scan", null, true, false, false, false));

		$.sleep(6000);
		conn.callApi("image", null, true, true,false);
		
		$.writeln(conn.callApi("s2nclose", null, true, false, false, false));*/
		//--------------------------------------------------------------------------------------
		
		main.wireEvents();
		main.removeEvents();
	},
	
	createWindow : function () {
		var grpConnStatus = "", 
			grpConn = "", 
			spacer = "", 
			grpFormat = "", 
			grpScannerControl = "",
			grpProg = "",
			grpHis = "";
		
		main.win = new Window("palette {orientation: 'column', alignChildren: ['fill', 'top'], text: 'Scan2PS v: 1.1', closeButton: true}");
		main.loadWin = new Window("palette {orientation: 'column', alignChildren: ['fill', 'top'], preferredSize: [300,60] ,text: ''}");	
		grpConnStatus = main.win.add("panel {orientation: 'row', alignChildren: ['fill', 'top']}");
		main.lblConnStatus = grpConnStatus.add("statictext", undefined, "Connection status: no connection");
		main.btnHelp = grpConnStatus.add("button", [0,0,10,25], "Help");
		main.lblConnStatus.graphics.foregroundColor = main.lblConnStatus.graphics.newPen (main.lblConnStatus.graphics.PenType.SOLID_COLOR, [0.5, 0, 0], 1);
		grpConn = main.win.add("panel {orientation: 'column', alignChildren: ['fill', 'top']}");
		main.lblIp = grpConn.add("statictext {text: 'Scanner IP-Adress:', characters: 18, justify: 'center' }");
		main.inIpAddr = grpConn.add("edittext", undefined, "");
		main.lbLast = grpConn.add("statictext {text: 'Last used:', characters: 18, justify: 'center' }");
		grpHis = grpConn.add("panel {orientation: 'row', alignChildren: ['fill', 'top']}");
		main.drpLast = grpHis.add("dropdownlist", undefined, main.hisArr);
		main.drpLast.selection = main.hisArr.length-1;
		main.btnClear = grpHis.add("button", undefined, "Clear");
		spacer = grpConn.add("group", undefined);
		main.btnConn = grpConn.add("button", undefined, "Connect");
		grpFormat = main.win.add("panel");
		main.rdJpeg = grpFormat.add("radiobutton", undefined, "JPEG");
		main.rdJpeg.value = true;
		main.rdTiff = grpFormat.add("radiobutton", undefined, "TIFF");
		grpScannerControl = main.win.add("panel {orientation: 'row', alignChildren: ['fill', 'top']}");
		main.btnScan = grpScannerControl.add("button", undefined, "Start Scan", {name:"scan"});
		main.btnRe = grpScannerControl.add("button", undefined, "Load Image", {name:"image"});
		main.btnOpenWizard = grpScannerControl.add("button", undefined, "ScanWizard", {name: "wizard"});
		main.prog = main.loadWin.add("progressbar", [10,10,150,50], 0);
		main.btnStop = main.loadWin.add("button", undefined, "Stop Scan", {name:"scan"});
		main.btnClose = main.win.add("button", undefined, "Close");
		main.win.show();
	},
	
	wireEvents : function() {
		main.btnConn.onClick = main.connect;
		main.btnScan.onClick = main.scan;
		main.btnRe.onClick = main.rescan;
		main.drpLast.onChange = main.selHis;
		main.btnOpenWizard.onClick = conn.wizard;
		main.btnStop.onClick = main.stop;
		main.prog.onShow = main.resLoad;
		main.btnClear.onClick = main.clearHis;
		main.btnClose.onClick = main.closeWin;
		main.btnHelp.onClick = main.openHelp;
	},

	openHelp : function() {
	},

	closeWin : function() {
		main.win.hide();
		main.close = true;
	}, 

	removeEvents : function() {
		main.btnScan.onClick = function() {};
		main.btnRe.onClick = function() {};
		main.btnOpenWizard.onClick = function() {};
	},

	resLoad : function() {
		main.prog.value = 0;
	},

	getFormat : function(file) {
		if (main.rdJpeg.value) {
			if (file) {
				return JPEG_FILE_ENDING;
			} else {
				return JPEG_FORMAT;
			}
		} else {
			return TIFF;
		}
	},
	
	connect : function() {
		var info = "", host = "", tmpHost = "", hostIndex = 0;
		
		conn.ip = main.inIpAddr.text + ":" + HTTP_PORT;
		conn.encoding = "binary";
		info = conn.callApi("s2ninfo", null, false, false, true);

                
		if (info == CONN_ERR) {
			main.errorText();
			alert("Connection error");
		} else if (info.length >= 6) {
			
			// get all device types without stop button
			if (info[0].indexOf("52") != -1 || info[0].indexOf("62") != -1) {
				main.stopBtnFlag = false;
			} else {
				main.stopBtnFlag = true;
			}
			
              for (var  i = 0; i < info.length; i++) {
				if (info[i].indexOf("hostname:") != -1) {
						hostIndex = i;
				}
              }
            
			tmpHost = info[hostIndex].split(": ");
			if (tmpHost.length >= 2) {
				host = tmpHost[1];
				main.saveData(main.inIpAddr.text, host);
				main.lblConnStatus.text = "Connected to: " + host;
				main.lblConnStatus.graphics.foregroundColor = main.lblConnStatus.graphics.newPen (main.lblConnStatus.graphics.PenType.SOLID_COLOR, [0, 0.5, 0], 1);
				main.wireEvents();
			} else {
				main.errorText();
				alert("Connection error");
				main.removeEvents();
			}
		} else {
			main.errorText();
			alert("Connection error");
			main.removeEvents();
		}
	},

	errorText  : function() {
		main.lblConnStatus.text = "Connection status: no connection";
		main.lblConnStatus.graphics.foregroundColor = main.lblConnStatus.graphics.newPen (main.lblConnStatus.graphics.PenType.SOLID_COLOR, [0.5, 0, 0], 1);
	}, 

	openSession : function() {
		var sessArr = [];
		sessArr = (conn.callApi("s2nopen", null, false, false, false)).split("ID: ");
		
		// catch connection and in use error
		if (sessArr.length >= 1) {
			if (sessArr[1].indexOf("ERROR") == -1) {			
				conn.sessionId = sessArr[1]; 
				return true;
			} else {
				main.loadWin.hide();
				alert("Scanner in use");
				return false;
			}
		} else {
			main.loadWin.hide();
			alert("Connection error");
			return false;
		}
	
		main.loadWin.hide();
	},

	scan : function() {		
		var res = "";

		main.btnStop.visible = main.stopBtnFlag;
		main.loadWin.show();
		main.loadWin.text = "Scanning";
		main.openSession();
		main.removeEvents();		
		res = conn.callApi("scan", null, true, false, false, false);
						
		//if (res.indexOf("Status: OK") != -1) {
			//main.scanned = true;
		/*} else */if (res.indexOf("ERROR") != -1){
			main.loadWin.hide();
			alert("Scanning error");
			main.wireEvents();
		}/* else {
			main.loadWin.hide();
			main.wireEvents();
		}*/
		
		main.scanned = true;
	},

	rescan : function() {
		main.btnStop.visible = false;
		main.openSession();
		conn.loadImg();
	},

	stop : function() {		
		conn.callApi("JavaCallds", "DS_SET+DS_STOPBTN", false, false, false);
		$.sleep(1);
		conn.callApi("JavaCallds", "DS_CLEAR+DS_STOPBTN", false, false, false);
	},

	readHisFile : function() {
		var rfile =  new File(Folder.userData + HISTORY_SAVE_FILE), 
			data = "";
			
		rfile.open("r");
		
		while(!rfile.eof) {
			data += rfile.readln();
		}
	
		rfile.close();
		return data;
	},

	saveData : function(ip, host) {
		var sfile =  new File(Folder.userData + HISTORY_SAVE_FILE),
			data = main.readHisFile(), 
			tmpArr = [];
				
		sfile.open("w");

		if (data.indexOf(ip) == -1) {
			sfile.write(data + HISTORY_SEPERATOR + ip + HISTORY_ENTRY_SEPERATOR + host);
		} else {
			sfile.write(data);
		}
		sfile.close;
	},

	getData : function() {
		var data = main.readHisFile(), 
			tmpArr = [],
			line = [],
			arr = [];
		
		tmpArr = data.split(HISTORY_SEPERATOR);
		
		if (tmpArr[0] != "" || tmpArr.length > 0) {	// todo check this
			
			// We have to start at 1, because the first entry in the file is a seperator
			for (var i = 1; i < tmpArr.length; i++) {
				line = tmpArr[i].split("_");
				
				if (line.length >= 1) {
					arr.push(line[0] + " " + line[1]);
				}
			}				
		} 
	
		return arr;			
	},

	clearHis : function() {				
		var sfile =  new File(Folder.userData + HISTORY_SAVE_FILE);
		sfile.open("w");
		sfile.write("");
				
		main.init();
	},

	selHis : function() {
		var tmp = "", 
			ip = "",
			arr = [];
		
		if (main.drpLast.selection != null) {
			tmp = main.drpLast.selection.text; 
		}
		
		arr = tmp.split(" "); 
		
		if (arr.length >= 1) {
			ip = arr[0];
		}
		
		main.inIpAddr.text = ip;
	},
};

var conn = {
	ip : "",
	encoding : "",
	sessionId : "",
	
	callApi : function(func, param, useSessionId, getBin, getArr) {
		var send  = "";
		
		if (ip = "")
			return CONN_ERR;
		
		currSocket = new Socket(PORT);
		currSocket.encoding = conn.encoding;
		
		if (func == IMAGE_FUNCTION) {
			currSocket.timeout = IMAGE_TIMEOUT;
		} else {
			currSocket.timeout = TIMEOUT;
		}
	
		// build the send string
		if (currSocket.open(conn.ip) && func != null) {
			send =  CGI_GET + func;
					
			if (param != null) {				
				if (!useSessionId) {
					send += CGI_PARAM_START + param;
				} else if (useSessionId) {
					send += CGI_PARAM_START + conn.sessionId + CGI_PARAM_CONTINUE + param;
				}
			}
		
			if (useSessionId && param == null) {				
				send += CGI_PARAM_START + conn.sessionId; 
			}
		} else {
			return CONN_ERR;
		}

		send = send.replace(/\r?\n|\r/g, '');						
		send += " HTTP/1.0\r\n\r\n";		
				
		currSocket.write(send);
		return conn.getData(getBin, getArr, currSocket);
	},

	getData : function(getBin, getArr, currSocket) {
		var path = "", 
			homeDir = "",
			homeDirArr = [],
			homeDirNoDev = "",
			sFile = "",
			data = "",
			dataArr = [], 
			retDataArr = [];
				
		if (!getBin) {
			data = currSocket.read(1024*1024*10);
			
		// when the binary mode is active, we will download the image to a file
		} else if (getBin) {
			homeDir = Folder.myDocuments.fsName.split("C:\\");
			homeDirArr = homeDir;
			
			if (homeDirArr.length >= 1) {
				homeDirNoDev = homeDirArr[1];
			} else {
				return CONN_ERROR;
			}
					
			path = "D:\\Scanner_Workspace" + 
				"\\" + IMG_FILENAME + new Date().getTime()+ "." + main.getFormat(true);
				
			sFile = new File(path);
			sFile.encoding = IMG_ENCODING;
			sFile.open("w");
			main.loadWin.text = "Getting Image"
			main.loadWin.show();
			
			while(true) {	
				data = currSocket.read(IMG_BLOCK_SIZE);
				if (data.indexOf("ERROR") != -1) {
					alert("Error getting image");
				}
			
				if (data.indexOf("supported") != -1) {
					alert("File format not supported");
				}
				
				if (data.length == 0) {
					break; 
				}
				
				sFile.write(conn.removeHeaders(data));
			}
		
			sFile.close();
			currSocket.close();
			return path;
		} else {
			currSocket.close();
		}
				
		/* if we have no image, and no string array to get, we need just line 6, a one line string (the first
		positions are http headers and stuff)*/
		if (!getBin && !getArr) {		
			dataArr = data.split("\n");			
			return dataArr[6]; // don't change this magic number, read comment above
		} else if (getArr) {
			dataArr = data.split("\n");
			retDataArr = dataArr.slice(6); // same here
			return retDataArr;
		} else {
			return path
		}
	},

	removeHeaders : function (bin) {
		var bContinue = true, 
			line = "", 
			nFirst = 0, 
			count = 0, n;
	
		n = bin.indexOf("\r\n\r\n");	
		line=bin.substring(n+4);
		return line;
	},

	checkImg : function() {
		res = conn.callApi("check", "image", true, false, true);
		
		if (res.length == 0) {
			return false;
		} else {
			return true;
		}
	},

	loadImg : function() {
		var path = "", imgFile = "";
		
		conn.callApi("set", "fileformat:" + main.getFormat(false), true, false, false);
		conn.callApi("set", "tiff_compr:none+colormode:truecolor", true, false, false);
		path = conn.callApi("image", null, true, true,false);
		conn.callApi("s2nclose", null, true, false, false, false);
		imgFile = new File(path);
		main.prog.value = 1000;
		
	try {
			app.open(imgFile); 
		} catch(e) {}
		
		main.loadWin.hide();
	},

	wizard : function() {
		var url = conn.ip + WIZARD;
	
		if ($.os.indexOf(WIN) != -1)  {
			app.system("cmd.exe /c\"start http://"+ url +"\"");		
		} else {
			system.callSystem("open http://"+site);
		}
	}
};

main.init();
start();

function start() {
	main.win.onClose = function() {
		return main.close = true;
	};

	var counter = 0;

	while(!main.close) {		
		counter++;
	
		$.sleep(500);
		try {
			app.refresh();
		} catch (e) {}
		
		if (main.scanned) {		
			main.prog.value = main.prog.value + LOAD_BAR_STEPS;
			
			if (conn.checkImg()) {
				main.prog.value = 1000;
				conn.loadImg();
				main.scanned = false;
				main.loadWin.hide();
				main.prog.value = 0;
				main.wireEvents();
			}
		}
	}

	return false;
}