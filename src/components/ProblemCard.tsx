import React from 'react';
import { Problem, Solution } from '../types';
import { ArrowRight, Bookmark, Sparkles, CheckCircle2 } from 'lucide-react';

interface ProblemCardProps {
  problem: Problem;
  solution?: Solution;
  onSelect: (problemId: string) => void;
  isSaved: boolean;
  onToggleSave: (problemId: string, e: React.MouseEvent) => void;
}

export const ProblemCard: React.FC<ProblemCardProps> = ({
  problem,
  solution,
  onSelect,
  isSaved,
  onToggleSave,
}) => {
  const getBadgeColor = (category: string) => {
    switch (category) {
      case 'Distractions':
        return 'bg-amber-50 text-amber-700 border-amber-200';
      case 'Time Management':
        return 'bg-blue-50 text-blue-700 border-blue-200';
      case 'Notes & Material':
        return 'bg-emerald-50 text-emerald-700 border-emerald-200';
      case 'Revision & Memory':
        return 'bg-purple-50 text-purple-700 border-purple-200';
      case 'Exam Preparation':
        return 'bg-rose-50 text-rose-700 border-rose-200';
      default:
        return 'bg-slate-50 text-slate-700 border-slate-200';
    }
  };

  return (
    <div 
      onClick={() => onSelect(problem.id)}
      className="group relative bg-white border border-slate-200 hover:border-blue-400 rounded-2xl p-6 transition-all duration-200 hover:shadow-md hover:-translate-y-0.5 cursor-pointer flex flex-col justify-between"
    >
      <div>
        {/* Top meta row */}
        <div className="flex items-center justify-between gap-2 mb-3">
          <span className={`inline-flex items-center px-2.5 py-0.5 rounded-full text-[11px] font-semibold border ${getBadgeColor(problem.category)}`}>
            {problem.category}
          </span>
          <button
            onClick={(e) => onToggleSave(problem.id, e)}
            className={`p-1.5 rounded-lg transition-colors ${
              isSaved
                ? 'text-blue-600 bg-blue-50'
                : 'text-slate-400 hover:text-slate-600 hover:bg-slate-100'
            }`}
            title={isSaved ? 'Saved to My Focus' : 'Save to My Focus'}
            aria-label="Save solution"
          >
            <Bookmark className={`w-4 h-4 ${isSaved ? 'fill-blue-600' : ''}`} />
          </button>
        </div>

        {/* Problem Title */}
        <h3 className="text-base sm:text-lg font-bold text-slate-900 group-hover:text-blue-600 transition-colors leading-snug line-clamp-2">
          {problem.title}
        </h3>

        {/* Summary */}
        <p className="text-sm text-slate-600 mt-2 leading-relaxed line-clamp-2">
          {problem.shortSummary}
        </p>

        {/* Symptoms sneak peek */}
        <div className="mt-3.5 space-y-1">
          {problem.commonSymptoms.slice(0, 1).map((symptom, idx) => (
            <div key={idx} className="flex items-start gap-1.5 text-xs text-slate-500">
              <span className="text-amber-500 font-bold">•</span>
              <span className="line-clamp-1 italic">"{symptom}"</span>
            </div>
          ))}
        </div>
      </div>

      {/* Bottom Recommendation Teaser */}
      <div className="mt-5 pt-4 border-t border-slate-100">
        <div className="flex items-center justify-between">
          <div className="flex items-center gap-1.5 text-xs text-slate-600">
            <Sparkles className="w-3.5 h-3.5 text-blue-600" />
            <span>Recommended:</span>
            <span className="font-semibold text-slate-900">
              {solution ? solution.name : 'Vetted Tool'}
            </span>
            {solution?.isCompletelyFree && (
              <span className="hidden sm:inline-flex items-center gap-0.5 text-[10px] font-medium text-emerald-600 bg-emerald-50 px-1.5 py-0.5 rounded">
                <CheckCircle2 className="w-2.5 h-2.5" /> Free
              </span>
            )}
          </div>

          <div className="flex items-center text-xs font-semibold text-blue-600 group-hover:translate-x-0.5 transition-transform">
            <span>View Solution</span>
            <ArrowRight className="w-3.5 h-3.5 ml-1" />
          </div>
        </div>
      </div>
    </div>
  );
};
