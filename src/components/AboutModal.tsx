import React from 'react';
import { Target, X, Check, User } from 'lucide-react';

interface AboutModalProps {
  isOpen: boolean;
  onClose: () => void;
}

export const AboutModal: React.FC<AboutModalProps> = ({ isOpen, onClose }) => {
  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-900/40 backdrop-blur-sm animate-in fade-in duration-200">
      <div className="bg-white rounded-2xl max-w-xl w-full max-h-[90vh] flex flex-col shadow-2xl border border-slate-200 overflow-hidden">
        
        {/* Header */}
        <div className="p-6 border-b border-slate-100 flex items-center justify-between">
          <div className="flex items-center gap-3">
            <div className="w-10 h-10 rounded-xl bg-blue-600 text-white flex items-center justify-center">
              <Target className="w-5 h-5 text-white" />
            </div>
            <div>
              <h3 className="text-lg font-bold text-slate-900">About Liteage Focus</h3>
              <p className="text-xs text-blue-600 font-medium">Find your solution. Focus on your goals.</p>
            </div>
          </div>
          <button
            onClick={onClose}
            className="text-slate-400 hover:text-slate-600 p-1.5 rounded-lg hover:bg-slate-100 transition-colors"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Content */}
        <div className="p-6 overflow-y-auto space-y-5 text-slate-700 text-sm leading-relaxed">
          <div>
            <h4 className="font-bold text-slate-900 mb-1">Why Liteage Focus Exists</h4>
            <p className="text-slate-600">
              Students struggle to find suitable digital solutions for their academic and productivity problems. Useful resources are scattered across the internet, many tools do not suit laptop or mobile routines, and critical features are frequently locked behind expensive subscriptions.
            </p>
          </div>

          <div className="p-4 bg-slate-50 rounded-xl border border-slate-200 space-y-2.5">
            <h4 className="font-bold text-slate-900 text-xs uppercase tracking-wider">Our Core Philosophy</h4>
            <div className="space-y-2 text-xs">
              <div className="flex items-start gap-2">
                <Check className="w-4 h-4 text-blue-600 shrink-0 mt-0.5" />
                <span><strong>Problem-First:</strong> Organized by what you struggle with, not app names.</span>
              </div>
              <div className="flex items-start gap-2">
                <Check className="w-4 h-4 text-emerald-600 shrink-0 mt-0.5" />
                <span><strong>Free-First:</strong> Prioritizing genuine 100% free or generous student tiers.</span>
              </div>
              <div className="flex items-start gap-2">
                <Check className="w-4 h-4 text-indigo-600 shrink-0 mt-0.5" />
                <span><strong>One Clear Recommendation:</strong> No analysis paralysis; one primary vetted pick with honest alternatives.</span>
              </div>
              <div className="flex items-start gap-2">
                <Check className="w-4 h-4 text-amber-600 shrink-0 mt-0.5" />
                <span><strong>Zero AI Fluff:</strong> No synthetic chatbots or automated hallucinations; every recommendation is verified.</span>
              </div>
            </div>
          </div>

          <div className="border-t border-slate-100 pt-4">
            <h4 className="font-bold text-slate-900 mb-1 flex items-center gap-1.5">
              <User className="w-4 h-4 text-blue-600" />
              Creator Information
            </h4>
            <p className="text-xs text-slate-600 leading-relaxed">
              Designed & developed by <strong>Shivendra Kumar Sharma</strong> (Class 12, Nav Jeevan Mission School, Kasia) for the <strong>Youth Ideathon India Challenge (YIIC 9)</strong>.
            </p>
          </div>
        </div>

        {/* Footer */}
        <div className="p-4 bg-slate-50 border-t border-slate-100 flex justify-end">
          <button
            onClick={onClose}
            className="px-5 py-2.5 bg-blue-600 hover:bg-blue-700 text-white rounded-xl font-medium text-sm transition-colors shadow-sm"
          >
            Got It
          </button>
        </div>

      </div>
    </div>
  );
};
