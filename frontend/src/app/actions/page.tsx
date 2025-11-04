"use client";

import { useState } from "react";
import { motion } from "framer-motion";
import Link from "next/link";

export default function ActionsPage() {
  const [selectedCategory, setSelectedCategory] = useState<string>("all");

  const categories = [
    { id: "all", name: "Tất cả", icon: "🌱" },
    { id: "energy", name: "Năng lượng", icon: "⚡" },
    { id: "waste", name: "Rác thải", icon: "♻️" },
    { id: "transport", name: "Giao thông", icon: "🚲" },
    { id: "water", name: "Nước", icon: "💧" },
  ];

  const actions = [
    {
      id: 1,
      title: "Sử dụng năng lượng mặt trời",
      category: "energy",
      impact: "Cao",
      description: "Lắp đặt tấm pin mặt trời để giảm lượng khí thải carbon và tiết kiệm chi phí điện năng.",
      icon: "☀️",
      difficulty: "Trung bình",
      estimatedImpact: "Giảm 2-3 tấn CO2/năm",
    },
    {
      id: 2,
      title: "Phân loại rác tại nguồn",
      category: "waste",
      impact: "Trung bình",
      description: "Phân loại rác thải thành các loại: hữu cơ, tái chế, và rác thải thông thường.",
      icon: "🗑️",
      difficulty: "Dễ",
      estimatedImpact: "Giảm 30% lượng rác thải",
    },
    {
      id: 3,
      title: "Đi xe đạp hoặc đi bộ",
      category: "transport",
      impact: "Cao",
      description: "Sử dụng phương tiện giao thông không phát thải cho các quãng đường ngắn.",
      icon: "🚴",
      difficulty: "Dễ",
      estimatedImpact: "Giảm 1-2 tấn CO2/năm",
    },
    {
      id: 4,
      title: "Tiết kiệm nước",
      category: "water",
      impact: "Trung bình",
      description: "Sử dụng các thiết bị tiết kiệm nước và tái sử dụng nước khi có thể.",
      icon: "💧",
      difficulty: "Dễ",
      estimatedImpact: "Tiết kiệm 20-30% lượng nước",
    },
    {
      id: 5,
      title: "Trồng cây xanh",
      category: "all",
      impact: "Cao",
      description: "Trồng cây xanh trong nhà và xung quanh khu vực sống để cải thiện chất lượng không khí.",
      icon: "🌳",
      difficulty: "Dễ",
      estimatedImpact: "Hấp thụ 50-100kg CO2/năm",
    },
    {
      id: 6,
      title: "Sử dụng túi vải thay vì túi nilon",
      category: "waste",
      impact: "Trung bình",
      description: "Mang theo túi vải khi đi mua sắm để giảm sử dụng túi nhựa dùng một lần.",
      icon: "🛍️",
      difficulty: "Dễ",
      estimatedImpact: "Giảm 100-200 túi nhựa/năm",
    },
  ];

  const filteredActions = selectedCategory === "all" 
    ? actions 
    : actions.filter(action => action.category === selectedCategory);

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
                🌱 Hành động xanh
              </h1>
            </div>
            <nav className="hidden md:flex items-center gap-6">
              <Link href="/map" className="text-sm text-gray-600 hover:text-success-600 dark:text-gray-400 dark:hover:text-success-400">
                Bản đồ
              </Link>
              <Link href="/stats" className="text-sm text-gray-600 hover:text-success-600 dark:text-gray-400 dark:hover:text-success-400">
                Thống kê
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
        <div className="mb-8 text-center">
          <motion.h2
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            className="mb-4 text-3xl font-bold text-gray-900 dark:text-white"
          >
            Hành động xanh được đề xuất bởi AI
          </motion.h2>
          <motion.p
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.1 }}
            className="max-w-2xl mx-auto text-gray-600 dark:text-gray-400"
          >
            Dựa trên vị trí và dữ liệu môi trường của bạn, đây là các hành động xanh được đề xuất để cải thiện môi trường sống.
          </motion.p>
        </div>

        {/* Filter Bar */}
        <div className="mb-8">
          <div className="flex flex-wrap gap-3 justify-center">
            {categories.map((category) => (
              <motion.button
                key={category.id}
                onClick={() => setSelectedCategory(category.id)}
                whileHover={{ scale: 1.05 }}
                whileTap={{ scale: 0.95 }}
                className={`px-6 py-3 rounded-xl font-medium transition-all ${
                  selectedCategory === category.id
                    ? "bg-gradient-to-r from-success-500 to-success-600 text-white shadow-lg"
                    : "bg-white dark:bg-gray-800 text-gray-700 dark:text-gray-300 border border-gray-200 dark:border-gray-700 hover:border-success-500"
                }`}
              >
                <span className="mr-2">{category.icon}</span>
                {category.name}
              </motion.button>
            ))}
          </div>
        </div>

        {/* Actions Grid */}
        <div className="grid grid-cols-1 gap-6 md:grid-cols-2 lg:grid-cols-3">
          {filteredActions.map((action, index) => (
            <motion.div
              key={action.id}
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: index * 0.1 }}
              whileHover={{ y: -5 }}
              className="p-6 bg-white dark:bg-gray-800 rounded-xl shadow-lg hover:shadow-xl transition-shadow border border-gray-200 dark:border-gray-700"
            >
              <div className="flex items-start justify-between mb-4">
                <div className="text-4xl">{action.icon}</div>
                <span className={`px-3 py-1 text-xs font-semibold rounded-full ${
                  action.impact === "Cao"
                    ? "bg-success-100 text-success-700 dark:bg-success-500/20 dark:text-success-400"
                    : "bg-warning-100 text-warning-700 dark:bg-warning-500/20 dark:text-warning-400"
                }`}>
                  Tác động: {action.impact}
                </span>
              </div>
              
              <h3 className="mb-2 text-xl font-semibold text-gray-900 dark:text-white">
                {action.title}
              </h3>
              
              <p className="mb-4 text-gray-600 dark:text-gray-400">
                {action.description}
              </p>
              
              <div className="space-y-2 pt-4 border-t border-gray-200 dark:border-gray-700">
                <div className="flex items-center justify-between text-sm">
                  <span className="text-gray-600 dark:text-gray-400">Độ khó:</span>
                  <span className="font-medium text-gray-900 dark:text-white">{action.difficulty}</span>
                </div>
                <div className="flex items-center justify-between text-sm">
                  <span className="text-gray-600 dark:text-gray-400">Tác động ước tính:</span>
                  <span className="font-medium text-success-600 dark:text-success-400">{action.estimatedImpact}</span>
                </div>
              </div>
            </motion.div>
          ))}
        </div>

        {filteredActions.length === 0 && (
          <div className="py-12 text-center">
            <p className="text-gray-500 dark:text-gray-400">
              Không có hành động nào trong danh mục này.
            </p>
          </div>
        )}
      </div>
    </div>
  );
}

