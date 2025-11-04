"use client";

import { useState, Suspense } from "react";
import { useAirQuality, useAirQualityAlerts } from "@/hooks/useAirQuality";
import { AlertCircle, Loader2, MapPin } from "lucide-react";

function AirQualityContent() {
  const [skip, setSkip] = useState(0);
  const limit = 10;
  const { data: airQualityData, isLoading, error } = useAirQuality("Hanoi", skip, limit);
  const { data: alerts, isLoading: alertsLoading } = useAirQualityAlerts(150);

  const getAQIColor = (aqi: number) => {
    if (aqi <= 50) return "bg-green-100 text-green-800 border-green-300";
    if (aqi <= 100) return "bg-yellow-100 text-yellow-800 border-yellow-300";
    if (aqi <= 150) return "bg-orange-100 text-orange-800 border-orange-300";
    if (aqi <= 200) return "bg-red-100 text-red-800 border-red-300";
    return "bg-purple-100 text-purple-800 border-purple-300";
  };

  const getAQILabel = (aqi: number) => {
    if (aqi <= 50) return "Tốt";
    if (aqi <= 100) return "Trung bình";
    if (aqi <= 150) return "Không tốt cho nhóm nhạy cảm";
    if (aqi <= 200) return "Không tốt";
    return "Rất không tốt";
  };

  return (
    <main className="min-h-screen bg-gradient-to-b from-green-50 to-white p-6">
      <div className="max-w-6xl mx-auto">
        {/* Header */}
        <div className="mb-8">
          <h1 className="text-4xl font-bold text-green-800 mb-2">
            🌍 Bản đồ Chất Lượng Không Khí
          </h1>
          <p className="text-gray-600">
            Theo dõi chất lượng không khí tại các khu vực Hà Nội
          </p>
        </div>

        {/* Alerts Section */}
        {(alerts?.length ?? 0) > 0 && (
          <div className="mb-6 p-4 bg-red-50 border border-red-300 rounded-lg">
            <div className="flex items-start gap-2">
              <AlertCircle className="text-red-600 mt-1 flex-shrink-0" size={20} />
              <div>
                <h3 className="font-semibold text-red-900 mb-2">
                  ⚠️ Cảnh báo Chất Lượng Không Khí
                </h3>
                <div className="space-y-1">
                  {alerts?.map((alert: any, idx: number) => (
                    <p key={idx} className="text-sm text-red-800">
                      <strong>{alert.location}</strong>: AQI {alert.aqi_value} ({alert.aqi_level})
                    </p>
                  ))}
                </div>
              </div>
            </div>
          </div>
        )}

        {/* Loading State */}
        {isLoading && (
          <div className="flex items-center justify-center py-12">
            <Loader2 className="animate-spin text-green-600" size={32} />
            <span className="ml-3 text-gray-600">Đang tải dữ liệu...</span>
          </div>
        )}

        {/* Error State */}
        {error && (
          <div className="text-center py-12 text-red-600">
            <p>Lỗi tải dữ liệu. Vui lòng thử lại.</p>
          </div>
        )}

        {/* Air Quality Grid */}
        {!isLoading && airQualityData && (
          <div>
            <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-3">
              {airQualityData.items?.map((item: any) => (
                <div
                  key={item.id}
                  className={`p-4 rounded-lg border-2 transition-all hover:shadow-lg ${getAQIColor(item.aqi)}`}
                >
                  <div className="flex items-start justify-between mb-2">
                    <div>
                      <h3 className="font-semibold text-lg">{item.ward_name}</h3>
                      {item.district && <p className="text-sm opacity-75">{item.district}</p>}
                    </div>
                    <MapPin size={20} />
                  </div>

                  <div className="space-y-1 text-sm mb-3">
                    <div className="flex justify-between">
                      <span>AQI:</span>
                      <strong>{item.aqi.toFixed(1)}</strong>
                    </div>
                    {item.pm25 && (
                      <div className="flex justify-between">
                        <span>PM2.5:</span>
                        <span>{item.pm25.toFixed(1)} μg/m³</span>
                      </div>
                    )}
                    {item.pm10 && (
                      <div className="flex justify-between">
                        <span>PM10:</span>
                        <span>{item.pm10.toFixed(1)} μg/m³</span>
                      </div>
                    )}
                  </div>

                  <div className="bg-white bg-opacity-50 px-2 py-1 rounded text-xs font-medium text-center">
                    {getAQILabel(item.aqi)}
                  </div>
                </div>
              ))}
            </div>

            {/* Pagination */}
            <div className="flex justify-center gap-2 mt-8">
              <button
                disabled={skip === 0}
                onClick={() => setSkip(Math.max(0, skip - limit))}
                className="px-4 py-2 bg-green-600 text-white rounded disabled:opacity-50 disabled:cursor-not-allowed"
              >
                Trước
              </button>
              <span className="px-4 py-2">
                Trang {Math.floor(skip / limit) + 1}
              </span>
              <button
                disabled={(airQualityData.items?.length ?? 0) < limit}
                onClick={() => setSkip(skip + limit)}
                className="px-4 py-2 bg-green-600 text-white rounded disabled:opacity-50 disabled:cursor-not-allowed"
              >
                Tiếp
              </button>
            </div>
          </div>
        )}

        {/* Stats */}
        {!isLoading && airQualityData && (
          <div className="grid grid-cols-3 gap-4 mt-8 pt-8 border-t">
            <div className="text-center">
              <p className="text-2xl font-bold text-green-600">
                {airQualityData.total}
              </p>
              <p className="text-gray-600">Tổng khu vực</p>
            </div>
            <div className="text-center">
              <p className="text-2xl font-bold text-orange-600">
                {alerts?.length ?? 0}
              </p>
              <p className="text-gray-600">Cảnh báo</p>
            </div>
            <div className="text-center">
              <p className="text-2xl font-bold text-blue-600">
                {(airQualityData.items?.reduce((sum: number, item: any) => sum + item.aqi, 0) / airQualityData.items.length).toFixed(1)}
              </p>
              <p className="text-gray-600">AQI Trung bình</p>
            </div>
          </div>
        )}
      </div>
    </main>
  );
}

export default function MapPage() {
  return (
    <Suspense fallback={<div className="flex items-center justify-center min-h-screen">Đang tải...</div>}>
      <AirQualityContent />
    </Suspense>
  );
}

