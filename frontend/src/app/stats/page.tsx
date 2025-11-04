"use client";

import { useState } from "react";
import { motion } from "framer-motion";
import Link from "next/link";
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer, RadarChart, PolarGrid, PolarAngleAxis, PolarRadiusAxis, Radar } from "recharts";

export default function StatsPage() {
  const [selectedRegion, setSelectedRegion] = useState("all");

  const regions = [
    { id: "all", name: "Tất cả", value: "all" },
    { id: "district1", name: "Quận 1", value: "district1" },
    { id: "district2", name: "Quận 2", value: "district2" },
    { id: "district3", name: "Quận 3", value: "district3" },
  ];

  const aqiData = [
    { name: "Quận 1", aqi: 65, temperature: 28, energy: 85, schools: 24 },
    { name: "Quận 2", aqi: 58, temperature: 27, energy: 92, schools: 18 },
    { name: "Quận 3", aqi: 72, temperature: 29, energy: 78, schools: 31 },
    { name: "Quận 4", aqi: 68, temperature: 28, energy: 88, schools: 22 },
    { name: "Quận 5", aqi: 62, temperature: 27, energy: 90, schools: 19 },
  ];

  const radarData = [
    { subject: "AQI", A: 65, B: 58, fullMark: 100 },
    { subject: "Nhiệt độ", A: 28, B: 27, fullMark: 40 },
    { subject: "Năng lượng xanh", A: 85, B: 92, fullMark: 100 },
    { subject: "Trường học", A: 24, B: 18, fullMark: 50 },
    { subject: "Khu vực xanh", A: 70, B: 75, fullMark: 100 },
  ];

  const stats = {
    totalAQI: 65,
    avgTemperature: 28,
    greenEnergy: 87,
    totalSchools: 124,
    greenActions: 450,
  };

  return (
    <div className="min-h-screen bg-gray-50 dark:bg-gray-900">
      {/* Header */}
      <header className="bg-white dark:bg-gray-950 border-b border-gray-200 dark:border-gray-800 sticky top-0 z-40">
        <div className="px-4 py-4 mx-auto max-w-7xl sm:px-6 lg:px-8">
          <div className="flex items-center justify-between">
            <div className="flex items-center gap-4">
              <Link href="/" className="flex items-center gap-2">
                <img src="/images/logo/logo.svg" alt="GreenEduMap" className="h-8 w-auto" />
                <span className="text-lg font-bold bg-gradient-to-r from-success-600 to-success-500 bg-clip-text text-transparent">
                  GreenEduMap
                </span>
              </Link>
              <span className="text-gray-400">|</span>
              <h1 className="text-xl font-semibold text-gray-900 dark:text-white">
                📊 Thống kê khu vực
              </h1>
            </div>
            <nav className="hidden md:flex items-center gap-6">
              <Link href="/map" className="text-sm text-gray-600 hover:text-success-600 dark:text-gray-400 dark:hover:text-success-400">
                Bản đồ
              </Link>
              <Link href="/actions" className="text-sm text-gray-600 hover:text-success-600 dark:text-gray-400 dark:hover:text-success-400">
                Hành động xanh
              </Link>
              <Link href="/chat" className="text-sm text-gray-600 hover:text-success-600 dark:text-gray-400 dark:hover:text-success-400">
                Chat AI
              </Link>
            </nav>
          </div>
        </div>
      </header>

      <div className="px-4 py-8 mx-auto max-w-7xl sm:px-6 lg:px-8">
        {/* Intro Section */}
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          className="mb-8"
        >
          <h2 className="mb-4 text-3xl font-bold text-gray-900 dark:text-white">
            Tổng quan khu vực
          </h2>
          <p className="text-gray-600 dark:text-gray-400">
            So sánh các chỉ số môi trường và giáo dục giữa các khu vực
          </p>
        </motion.div>

        {/* Stats Cards */}
        <div className="grid grid-cols-1 gap-6 mb-8 md:grid-cols-2 lg:grid-cols-5">
          {[
            { label: "AQI trung bình", value: stats.totalAQI, unit: "", color: "success", icon: "🌬️" },
            { label: "Nhiệt độ", value: stats.avgTemperature, unit: "°C", color: "warning", icon: "🌡️" },
            { label: "Năng lượng xanh", value: stats.greenEnergy, unit: "%", color: "blue-light", icon: "⚡" },
            { label: "Trường học", value: stats.totalSchools, unit: "", color: "purple", icon: "🏫" },
            { label: "Hành động xanh", value: stats.greenActions, unit: "", color: "success", icon: "🌱" },
          ].map((stat, index) => (
            <motion.div
              key={stat.label}
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: index * 0.1 }}
              className="p-6 bg-white dark:bg-gray-800 rounded-xl shadow-lg"
            >
              <div className="flex items-center justify-between mb-2">
                <span className="text-2xl">{stat.icon}</span>
                <span className={`text-xs font-semibold px-2 py-1 rounded-full bg-${stat.color}-100 text-${stat.color}-700 dark:bg-${stat.color}-500/20 dark:text-${stat.color}-400`}>
                  {stat.label}
                </span>
              </div>
              <div className="text-3xl font-bold text-gray-900 dark:text-white">
                {stat.value}
                <span className="ml-1 text-lg text-gray-500">{stat.unit}</span>
              </div>
            </motion.div>
          ))}
        </div>

        {/* Region Filter */}
        <div className="mb-6">
          <label className="block mb-3 text-sm font-semibold text-gray-900 dark:text-white">
            Chọn khu vực
          </label>
          <div className="flex flex-wrap gap-3">
            {regions.map((region) => (
              <motion.button
                key={region.id}
                onClick={() => setSelectedRegion(region.value)}
                whileHover={{ scale: 1.05 }}
                whileTap={{ scale: 0.95 }}
                className={`px-4 py-2 rounded-xl font-medium transition-all ${
                  selectedRegion === region.value
                    ? "bg-gradient-to-r from-success-500 to-success-600 text-white shadow-lg"
                    : "bg-white dark:bg-gray-800 text-gray-700 dark:text-gray-300 border border-gray-200 dark:border-gray-700 hover:border-success-500"
                }`}
              >
                {region.name}
              </motion.button>
            ))}
          </div>
        </div>

        {/* Charts */}
        <div className="grid grid-cols-1 gap-6 lg:grid-cols-2">
          {/* Bar Chart */}
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.3 }}
            className="p-6 bg-white dark:bg-gray-800 rounded-xl shadow-lg"
          >
            <h3 className="mb-4 text-xl font-semibold text-gray-900 dark:text-white">
              So sánh chỉ số theo khu vực
            </h3>
            <ResponsiveContainer width="100%" height={400}>
              <BarChart data={aqiData}>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="name" />
                <YAxis />
                <Tooltip />
                <Legend />
                <Bar dataKey="aqi" fill="#22c55e" name="AQI" />
                <Bar dataKey="temperature" fill="#f59e0b" name="Nhiệt độ (°C)" />
                <Bar dataKey="energy" fill="#3b82f6" name="Năng lượng xanh (%)" />
                <Bar dataKey="schools" fill="#a855f7" name="Trường học" />
              </BarChart>
            </ResponsiveContainer>
          </motion.div>

          {/* Radar Chart */}
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.4 }}
            className="p-6 bg-white dark:bg-gray-800 rounded-xl shadow-lg"
          >
            <h3 className="mb-4 text-xl font-semibold text-gray-900 dark:text-white">
              Phân tích đa chiều
            </h3>
            <ResponsiveContainer width="100%" height={400}>
              <RadarChart data={radarData}>
                <PolarGrid />
                <PolarAngleAxis dataKey="subject" />
                <PolarRadiusAxis />
                <Radar name="Khu vực A" dataKey="A" stroke="#22c55e" fill="#22c55e" fillOpacity={0.6} />
                <Radar name="Khu vực B" dataKey="B" stroke="#3b82f6" fill="#3b82f6" fillOpacity={0.6} />
                <Legend />
              </RadarChart>
            </ResponsiveContainer>
          </motion.div>
        </div>
      </div>
    </div>
  );
}

