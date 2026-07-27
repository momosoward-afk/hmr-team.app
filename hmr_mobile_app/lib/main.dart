import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'webview_screen.dart';

void main() {
  WidgetsFlutterBinding.ensureInitialized();
  // Restrict app orientation to portrait only
  SystemChrome.setPreferredOrientations([
    DeviceOrientation.portraitUp,
    DeviceOrientation.portraitDown,
  ]);
  
  // Custom dark status bar overlay to match the premium theme
  SystemChrome.setSystemUIOverlayStyle(const SystemUiOverlayStyle(
    statusBarColor: Colors.transparent,
    statusBarIconBrightness: Brightness.light,
    systemNavigationBarColor: Color(0xFF070B14),
    systemNavigationBarIconBrightness: Brightness.light,
  ));
  
  runApp(const HmrApp());
}

class HmrApp extends StatelessWidget {
  const HmrApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'HMR Network',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        brightness: Brightness.dark,
        primaryColor: const Color(0xFF3B82F6),
        scaffoldBackgroundColor: const Color(0xFF070B14),
        colorScheme: const ColorScheme.dark(
          primary: Color(0xFF3B82F6),
          secondary: Color(0xFFFCD34D),
          surface: Color(0xFF1E293B),
        ),
      ),
      home: const WebviewScreen(),
    );
  }
}
