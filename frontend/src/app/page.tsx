"use client";
import Link from "next/link";
import { useState, useEffect } from "react";
import { motion } from "framer-motion";
import { 
  CheckCircleIcon,
  BoltIcon,
  BoxIcon,
  GroupIcon,
  ChevronDownIcon,
} from "@/icons";
import MapboxMap from "@/components/ui/map/MapboxMap";

export default function HomePage() {
  const [scrolled, setScrolled] = useState(false);
  const [mousePosition, setMousePosition] = useState({ x: 0, y: 0 });

  useEffect(() => {
    const handleScroll = () => {
      setScrolled(window.scrollY > 20);
    };
    const handleMouseMove = (e: MouseEvent) => {
      setMousePosition({ x: e.clientX, y: e.clientY });
    };
    
    window.addEventListener("scroll", handleScroll);
    window.addEventListener("mousemove", handleMouseMove);
    return () => {
      window.removeEventListener("scroll", handleScroll);
      window.removeEventListener("mousemove", handleMouseMove);
    };
  }, []);

  return (
    <div className="min-h-screen bg-gradient-to-br from-gray-50 via-white to-gray-50 dark:from-gray-950 dark:via-gray-900 dark:to-gray-950 overflow-x-hidden">
      {/* Animated Background */}
      <div className="fixed inset-0 overflow-hidden pointer-events-none">
        <motion.div
          className="absolute top-0 right-0 w-[800px] h-[800px] rounded-full opacity-20 bg-gradient-to-br from-success-400/40 to-transparent blur-3xl"
          animate={{
            x: mousePosition.x * 0.02,
            y: mousePosition.y * 0.02,
          }} 
          transition={{ type: "spring", stiffness: 50, damping: 30 }}
        />
        <motion.div
          className="absolute bottom-0 left-0 w-[600px] h-[600px] rounded-full opacity-20 bg-gradient-to-br from-blue-light-400/30 to-transparent blur-3xl"
          animate={{
            x: -mousePosition.x * 0.015,
            y: -mousePosition.y * 0.015,
          }}
          transition={{ type: "spring", stiffness: 50, damping: 30 }}
        />
      </div>

      {/* Navigation */}
      <motion.nav
        initial={{ y: -100 }}
        animate={{ y: 0 }}
        className={`fixed top-0 left-0 right-0 z-50 transition-all duration-500 ${
          scrolled
            ? "bg-white/80 dark:bg-gray-950/80 backdrop-blur-xl shadow-theme-lg border-b border-gray-200/50 dark:border-gray-800/50"
            : "bg-transparent"
        }`}
      >
        <div className="px-4 mx-auto max-w-7xl sm:px-6 lg:px-8">
          <div className="flex items-center justify-between h-16 sm:h-20">
            <motion.div 
              className="flex items-center gap-2"
              whileHover={{ scale: 1.05 }}
            >
              <img src="/images/logo/logo.svg" alt="GreenEduMap Logo" className="h-8 w-auto" />
            </motion.div>
            <div className="hidden gap-8 md:flex">
              {[
                { name: "Bản đồ", href: "/map" },
                { name: "Hành động xanh", href: "/actions" },
                { name: "Thống kê", href: "/stats" },
              ].map((item, index) => (
                <motion.a
                  key={item.name}
                  href={item.href}
                  className="text-sm font-medium text-gray-700 transition-colors hover:text-success-600 dark:text-gray-300 dark:hover:text-success-400 relative group"
                  initial={{ opacity: 0, y: -20 }}
                  animate={{ opacity: 1, y: 0 }}
                  transition={{ delay: index * 0.1 }}
                >
                  {item.name}
                  <span className="absolute bottom-0 left-0 w-0 h-0.5 bg-gradient-to-r from-success-500 to-success-600 transition-all group-hover:w-full" />
                </motion.a>
              ))}
            </div>
            <motion.div 
              className="flex items-center gap-3"
              initial={{ opacity: 0, x: 20 }}
              animate={{ opacity: 1, x: 0 }}
              transition={{ delay: 0.3 }}
            >
              <Link
                href="/login"
                className="px-4 py-2 text-sm font-medium text-gray-700 transition-all rounded-lg hover:bg-gray-100 dark:text-gray-300 dark:hover:bg-gray-800/50"
              >
                Đăng nhập
              </Link>
              <Link
                href="/register"
                className="px-4 py-2 text-sm font-medium text-white transition-all rounded-lg bg-gradient-to-r from-success-500 to-success-600 hover:shadow-lg hover:shadow-success-500/50 hover:scale-105"
              >
                Đăng ký
              </Link>
            </motion.div>
          </div>
        </div>
      </motion.nav>

      {/* Hero Section */}
      <section className="relative pt-24 pb-20 overflow-hidden sm:pt-32 sm:pb-32">
        <div className="absolute inset-0">
          <div className="absolute inset-0 bg-gradient-to-br from-white via-success-50/30 to-blue-light-50/20 dark:from-gray-950 dark:via-success-950/20 dark:to-blue-light-950/10" />
          <div className="absolute inset-0 bg-[url('/grid.svg')] opacity-[0.02] dark:opacity-[0.05]" />
        </div>

        <div className="relative px-4 mx-auto max-w-7xl sm:px-6 lg:px-8">
          <div className="text-center">
            <motion.div
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.6 }}
              className="inline-flex items-center gap-2 px-4 py-2 mb-6 rounded-full bg-gradient-to-r from-success-50 to-blue-light-50 dark:from-success-500/10 dark:to-blue-light-500/10 border border-success-200/50 dark:border-success-800/50 shadow-lg"
            >
              <span className="relative flex h-3 w-3">
                <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-success-400 opacity-75"></span>
                <span className="relative inline-flex rounded-full h-3 w-3 bg-success-500"></span>
              </span>
              <span className="text-sm font-medium bg-gradient-to-r from-success-600 to-blue-light-600 dark:from-success-400 dark:to-blue-light-400 bg-clip-text text-transparent">
                🌱 Bản đồ sống xanh & Giáo dục môi trường
              </span>
            </motion.div>
            
            <motion.h1
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.6, delay: 0.2 }}
              className="mb-6 font-bold text-gray-900 text-title-md sm:text-title-lg lg:text-title-xl dark:text-white"
            >
              Khám phá thành phố{" "}
              <span className="bg-gradient-to-r from-success-600 via-success-500 to-blue-light-500 bg-clip-text text-transparent animate-gradient">
                xanh của bạn
              </span>
            </motion.h1>
            
            <motion.p
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.6, delay: 0.4 }}
              className="max-w-3xl mx-auto mb-10 text-lg text-gray-600 sm:text-xl dark:text-gray-400"
            >
              GreenEduMap kết hợp bản đồ 3D thời gian thực về chất lượng không khí (AQI), 
              năng lượng xanh, và trường học với các gợi ý hành động xanh được đề xuất bởi AI 
              để xây dựng tương lai bền vững.
            </motion.p>
            
            <motion.div
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.6, delay: 0.6 }}
              className="flex flex-col items-center justify-center gap-4 sm:flex-row"
            >
              <motion.div whileHover={{ scale: 1.05 }} whileTap={{ scale: 0.95 }}>
                <Link
                  href="/map"
                  className="inline-flex items-center justify-center w-full px-6 py-4 text-base font-medium text-white transition-all rounded-xl shadow-xl bg-gradient-to-r from-success-500 via-success-600 to-blue-light-500 hover:shadow-2xl hover:shadow-success-500/50 sm:w-auto group"
                >
                  🗺️ Xem bản đồ
                  <motion.svg
                    className="w-5 h-5 ml-2"
                    fill="none"
                    viewBox="0 0 24 24"
                    stroke="currentColor"
                    whileHover={{ x: 5 }}
                  >
                    <path
                      strokeLinecap="round"
                      strokeLinejoin="round"
                      strokeWidth={2}
                      d="M13 7l5 5m0 0l-5 5m5-5H6"
                    />
                  </motion.svg>
                </Link>
              </motion.div>
              <motion.a
                href="#features"
                whileHover={{ scale: 1.05 }}
                whileTap={{ scale: 0.95 }}
                className="inline-flex items-center justify-center w-full px-6 py-4 text-base font-medium text-gray-700 transition-all bg-white/50 backdrop-blur-sm border border-gray-300 rounded-xl shadow-lg hover:bg-white/80 hover:shadow-xl sm:w-auto dark:bg-gray-800/50 dark:text-gray-300 dark:border-gray-700 dark:hover:bg-gray-800/80"
              >
                Tìm hiểu thêm
                <motion.div
                  animate={{ y: [0, 5, 0] }}
                  transition={{ duration: 1.5, repeat: Infinity }}
                >
                  <ChevronDownIcon className="w-5 h-5 ml-2" />
                </motion.div>
              </motion.a>
            </motion.div>
          </div>

          {/* Map Preview */}
          <motion.div
            initial={{ opacity: 0, y: 40 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.8, delay: 0.8 }}
            className="mt-16 sm:mt-24"
          >
            <div className="relative p-1 mx-auto rounded-2xl bg-gradient-to-r from-success-500 via-success-600 to-blue-light-500 max-w-6xl shadow-2xl hover:shadow-success-500/30 transition-shadow duration-500">
              <div className="overflow-hidden bg-white rounded-xl dark:bg-gray-900">
                <div className="aspect-video relative">
                  <MapboxMap className="w-full h-full" />
                </div>
              </div>
            </div>
          </motion.div>
        </div>
      </section>

      {/* Features Section */}
      <section id="features" className="py-20 bg-gradient-to-b from-gray-50 to-white dark:from-gray-900 dark:to-gray-950 sm:py-32 relative overflow-hidden">
        <div className="absolute inset-0 bg-[url('/grid.svg')] opacity-[0.02] dark:opacity-[0.03]" />
        
        <div className="px-4 mx-auto max-w-7xl sm:px-6 lg:px-8 relative">
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            transition={{ duration: 0.6 }}
            className="text-center mb-16"
          >
            <h2 className="mb-4 font-bold text-gray-900 text-title-sm sm:text-title-md dark:text-white">
              Tính năng{" "}
              <span className="bg-gradient-to-r from-success-600 to-success-500 bg-clip-text text-transparent">
                nổi bật
              </span>
            </h2>
            <p className="max-w-2xl mx-auto text-lg text-gray-600 dark:text-gray-400">
              Công nghệ hiện đại cho một thành phố xanh và bền vững
            </p>
          </motion.div>

          <div className="grid grid-cols-1 gap-8 md:grid-cols-2 lg:grid-cols-3">
            {[
              {
                icon: () => (
                  <svg className="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M3.055 11H5a2 2 0 012 2v1a2 2 0 002 2 2 2 0 012 2v2.945M8 3.935V5.5A2.5 2.5 0 0010.5 8h.5a2 2 0 012 2 2 2 0 104 0 2 2 0 012-2h1.064M15 20.488V18a2 2 0 012-2h3.064M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                  </svg>
                ),
                title: "Bản đồ 3D thời gian thực",
                desc: "Theo dõi chất lượng không khí (AQI), nhiệt độ, năng lượng xanh trên bản đồ 3D tương tác.",
                gradient: "from-success-500 to-success-600",
                bgGradient: "from-success-50 to-success-100 dark:from-success-500/10 dark:to-success-600/10",
                delay: 0,
              },
              {
                icon: () => (
                  <svg className="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z" />
                  </svg>
                ),
                title: "Gợi ý AI thông minh",
                desc: "Nhận đề xuất hành động xanh cá nhân hóa dựa trên vị trí và dữ liệu môi trường.",
                gradient: "from-success-500 to-success-600",
                bgGradient: "from-success-50 to-success-100 dark:from-success-500/10 dark:to-success-500/20",
                delay: 0.1,
              },
              {
                icon: () => (
                  <svg className="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253" />
                  </svg>
                ),
                title: "Khóa học môi trường",
                desc: "Học các khóa học về môi trường, phát triển bền vững từ các trường học và chuyên gia.",
                gradient: "from-blue-light-500 to-blue-light-600",
                bgGradient: "from-blue-light-50 to-blue-light-100 dark:from-blue-light-500/10 dark:to-blue-light-500/20",
                delay: 0.2,
              },
              {
                icon: () => (
                  <svg className="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M8 10h.01M12 10h.01M16 10h.01M9 16H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-5l-5 5v-5z" />
                  </svg>
                ),
                title: "Chat với GreenBot",
                desc: "Trò chuyện với AI GreenBot để nhận tư vấn về môi trường và hành động xanh.",
                gradient: "from-warning-500 to-orange-500",
                bgGradient: "from-warning-50 to-orange-50 dark:from-warning-500/10 dark:to-orange-500/10",
                delay: 0.3,
              },
              {
                icon: () => (
                  <svg className="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
                  </svg>
                ),
                title: "Thống kê & Phân tích",
                desc: "Xem biểu đồ so sánh khu vực, xu hướng môi trường và tác động hành động xanh.",
                gradient: "from-theme-purple-500 to-purple-600",
                bgGradient: "from-purple-50 to-purple-100 dark:from-purple-500/10 dark:to-purple-500/20",
                delay: 0.4,
              },
              {
                icon: GroupIcon,
                title: "Cộng đồng tham gia",
                desc: "Gửi ý tưởng xanh, chia sẻ kinh nghiệm và kết nối với cộng đồng yêu môi trường.",
                gradient: "from-theme-pink-500 to-pink-600",
                bgGradient: "from-pink-50 to-pink-100 dark:from-pink-500/10 dark:to-pink-500/20",
                delay: 0.5,
              },
            ].map((feature, index) => (
              <motion.div
                key={index}
                initial={{ opacity: 0, y: 30 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true }}
                transition={{ duration: 0.5, delay: feature.delay }}
                whileHover={{ y: -10, transition: { duration: 0.3 } }}
                className="relative p-8 overflow-hidden transition-all bg-white border border-gray-200 group rounded-2xl hover:shadow-2xl hover:shadow-success-500/10 dark:bg-gray-800/50 dark:border-gray-700 dark:hover:border-success-600/30 backdrop-blur-sm"
              >
                <div className={`absolute inset-0 bg-gradient-to-br ${feature.bgGradient} opacity-0 group-hover:opacity-100 transition-opacity duration-500`} />
                
                <div className="relative">
                  <motion.div
                    whileHover={{ rotate: 360, scale: 1.1 }}
                    transition={{ duration: 0.6 }}
                    className={`flex items-center justify-center w-14 h-14 mb-5 rounded-xl bg-gradient-to-br ${feature.gradient} shadow-lg`}
                  >
                    <feature.icon className="w-7 h-7 text-white" />
                  </motion.div>
                  <h3 className="mb-3 text-xl font-semibold text-gray-900 dark:text-white group-hover:text-success-700 dark:group-hover:text-success-400 transition-colors">
                    {feature.title}
                  </h3>
                  <p className="text-gray-600 dark:text-gray-400">
                    {feature.desc}
                  </p>
                </div>

                <div className={`absolute bottom-0 left-0 right-0 h-1 bg-gradient-to-r ${feature.gradient} opacity-0 group-hover:opacity-100 transition-opacity duration-500`} />
              </motion.div>
            ))}
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section className="relative py-20 overflow-hidden sm:py-32">
        <div className="absolute inset-0 bg-gradient-to-br from-success-600 via-success-500 to-blue-light-500"></div>
        <div className="absolute inset-0 bg-[url('/grid.svg')] opacity-10"></div>
        
        <div className="relative px-4 mx-auto text-center max-w-7xl sm:px-6 lg:px-8">
          <motion.h2
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            transition={{ duration: 0.6 }}
            className="mb-6 font-bold text-white text-title-sm sm:text-title-md drop-shadow-lg"
          >
            Sẵn sàng{" "}
            <span className="bg-gradient-to-r from-white to-brand-100 bg-clip-text text-transparent">
              hành động xanh
            </span>
            ?
          </motion.h2>
          <motion.p
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            transition={{ duration: 0.6, delay: 0.2 }}
            className="max-w-2xl mx-auto mb-10 text-lg text-white/90 sm:text-xl drop-shadow"
          >
            Tham gia cùng chúng tôi để xây dựng một thành phố xanh, 
            bền vững và thân thiện với môi trường hơn.
          </motion.p>
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            transition={{ duration: 0.6, delay: 0.4 }}
            className="flex flex-col items-center justify-center gap-4 sm:flex-row"
          >
            <motion.div whileHover={{ scale: 1.05 }} whileTap={{ scale: 0.95 }}>
              <Link
                href="/map"
                className="inline-flex items-center justify-center w-full px-8 py-4 text-base font-semibold transition-all bg-white rounded-xl shadow-2xl text-success-700 hover:bg-success-50 hover:shadow-white/30 sm:w-auto group"
              >
                Khám phá ngay
                <motion.svg
                  className="w-5 h-5 ml-2"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke="currentColor"
                  whileHover={{ x: 5 }}
                >
                  <path
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    strokeWidth={2}
                    d="M13 7l5 5m0 0l-5 5m5-5H6"
                  />
                </motion.svg>
              </Link>
            </motion.div>
            <motion.div whileHover={{ scale: 1.05 }} whileTap={{ scale: 0.95 }}>
              <Link
                href="/feedback"
                className="inline-flex items-center justify-center w-full px-8 py-4 text-base font-semibold text-white transition-all border-2 border-white/50 backdrop-blur-sm rounded-xl hover:bg-white/10 hover:border-white sm:w-auto"
              >
                Gửi ý tưởng xanh
              </Link>
            </motion.div>
          </motion.div>
        </div>
      </section>

      {/* Footer */}
      <footer className="py-12 bg-gradient-to-b from-gray-900 to-gray-950 border-t border-gray-800">
        <div className="px-4 mx-auto max-w-7xl sm:px-6 lg:px-8">
          <div className="grid grid-cols-1 gap-8 md:grid-cols-4">
            <div className="md:col-span-2">
              <motion.div
                initial={{ opacity: 0 }}
                whileInView={{ opacity: 1 }}
                viewport={{ once: true }}
                className="flex items-center gap-2 mb-4"
              >
                <img src="/images/logo/logo.svg" alt="GreenEduMap Logo" className="h-10 w-auto" />
              </motion.div>
              <p className="mb-4 text-gray-400">
                Bản đồ sống xanh & Giáo dục môi trường cho tương lai bền vững.
              </p>
              <p className="text-sm text-gray-500">
                © 2025 GreenEduMap. All rights reserved.
              </p>
            </div>

            <div>
              <h3 className="mb-4 text-sm font-semibold text-white uppercase tracking-wider">
                Khám phá
              </h3>
              <ul className="space-y-2">
                {[
                  { name: "Bản đồ", href: "/map" },
                  { name: "Hành động xanh", href: "/actions" },
                  { name: "Thống kê", href: "/stats" },
                ].map((item, index) => (
                  <motion.li
                    key={item.name}
                    initial={{ opacity: 0, x: -20 }}
                    whileInView={{ opacity: 1, x: 0 }}
                    viewport={{ once: true }}
                    transition={{ delay: index * 0.1 }}
                  >
                    <a
                      href={item.href}
                      className="text-gray-400 transition-colors hover:text-success-400 relative group inline-block"
                    >
                      {item.name}
                      <span className="absolute bottom-0 left-0 w-0 h-0.5 bg-gradient-to-r from-success-500 to-success-600 transition-all group-hover:w-full" />
                    </a>
                  </motion.li>
                ))}
              </ul>
            </div>

            <div>
              <h3 className="mb-4 text-sm font-semibold text-white uppercase tracking-wider">
                Liên hệ
              </h3>
              <ul className="space-y-2">
                {["Về chúng tôi", "Chat với AI", "Liên hệ"].map((item, index) => (
                  <motion.li
                    key={item}
                    initial={{ opacity: 0, x: -20 }}
                    whileInView={{ opacity: 1, x: 0 }}
                    viewport={{ once: true }}
                    transition={{ delay: index * 0.1 }}
                  >
                    <a
                      href={item === "Chat với AI" ? "/chat" : "#"}
                      className="text-gray-400 transition-colors hover:text-success-400 relative group inline-block"
                    >
                      {item}
                      <span className="absolute bottom-0 left-0 w-0 h-0.5 bg-gradient-to-r from-success-500 to-success-600 transition-all group-hover:w-full" />
                    </a>
                  </motion.li>
                ))}
              </ul>
            </div>
          </div>
        </div>
      </footer>
    </div>
  );
}
