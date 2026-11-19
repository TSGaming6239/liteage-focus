import React from 'react';
import { Problem, Solution } from '../types';
import { Bookmark, X, ArrowRight, Trash2 } from 'lucide-react';

interface SavedModalProps {
  isOpen: boolean;
  onClose: () => void;
  savedProblemIds: string[];
  problems: Problem[];
  solutions: Record<string, Solution>;
  onSelectProblem: (id: string) => void;
  onRemoveSaved: (id: string) => void;
}

export const SavedModal: React.FC<SavedModalProps> = ({
  isOpen,
  onClose,
  savedProblemIds,
  problems,
  solutions,
  onSelectProblem,
  onRemoveSaved,
}) => {
  if (!isOpen) return null;

  const savedProblems = problems.filter((p) => savedProblemIds.includes(p.id));

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-900/40 backdrop-blur-sm animate-in fade-in duration-200">
      <div className="bg-white rounded-2xl max-w-lg w-full max-h-[85vh] flex flex-col shadow-xl border border-slate-200 overflow-hidden">
        
        {/* Header */}
        <div className="p-5 border-b border-slate-100 flex items-center justify-between">
          <div className="flex items-center gap-2.5">
            <div className="w-9 h-9 rounded-xl bg-blue-50 text-blue-600 flex items-center justify-center">
              <Bookmark className="w-5 h-5 fill-blue-600" />
            </div>
            <div>
              <h3 className="text-base font-bold text-slate-900">My Saved Focus</h3>
              <p className="text-xs text-slate-500">
                {savedProblems.length} {savedProblems.length === 1 ? 'solution' : 'solutions'} saved in local storage
              </p>
            </div>
          </div>
          <button
            onClick={onClose}
            className="text-slate-400 hover:text-slate-600 p-1.5 rounded-lg hover:bg-slate-100 transition-colors"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* List of saved items */}
        <div className="p-5 overflow-y-auto space-y-3 flex-1">
          {savedProblems.length === 0 ? (
            <div className="text-center py-10">
              <div className="w-12 h-12 rounded-2xl bg-slate-100 text-slate-400 flex items-center justify-center mx-auto mb-3">
                <Bookmark className="w-6 h-6" />
              </div>
              <p className="text-sm font-semibold text-slate-700">No solutions saved yet</p>
              <p className="text-xs text-slate-500 mt-1 max-w-xs mx-auto">
                Click the bookmark icon on any problem or solution to save it to your local focus list for quick study access.
              </p>
            </div>
          ) : (
            savedProblems.map((problem) => {
              const sol = solutions[problem.recommendedSolutionId];
              return (
                <div
                  key={problem.id}
                  className="p-3.5 rounded-xl border border-slate-200 hover:border-blue-300 bg-white hover:bg-blue-50/30 transition-all flex items-center justify-between gap-3 group"
                >
                  <div 
                    onClick={() => {
                      onSelectProblem(problem.id);
                      onClose();
                    }}
                    className="flex-1 cursor-pointer"
                  >
                    <span className="text-[10px] font-semibold text-blue-600 uppercase tracking-wider">
                      {problem.category}
                    </span>
                    <h4 className="text-sm font-bold text-slate-900 group-hover:text-blue-600 transition-colors line-clamp-1">
                      {problem.title}
                    </h4>
                    <p className="text-xs text-slate-500 mt-0.5">
                      Tool: <span className="font-semibold text-slate-700">{sol?.name}</span> ({sol?.pricingStatus})
                    </p>
                  </div>

                  <div className="flex items-center gap-1">
                    <button
                      onClick={() => {
                        onSelectProblem(problem.id);
                        onClose();
                      }}
                      className="p-2 text-blue-600 hover:bg-blue-100 rounded-lg text-xs font-medium flex items-center gap-1"
                      title="Open problem"
                    >
                      <ArrowRight className="w-4 h-4" />
                    </button>
                    <button
                      onClick={() => onRemoveSaved(problem.id)}
                      className="p-2 text-slate-400 hover:text-rose-600 hover:bg-rose-50 rounded-lg transition-colors"
                      title="Remove from saved"
                    >
                      <Trash2 className="w-4 h-4" />
                    </button>
                  </div>
                </div>
              );
            })
          )}
        </div>

        {/* Footer */}
        <div className="p-4 bg-slate-50 border-t border-slate-100 flex items-center justify-between text-xs text-slate-500">
          <span>Saved locally on this device</span>
          <button
            onClick={onClose}
            className="px-4 py-2 bg-slate-200 hover:bg-slate-300 text-slate-800 rounded-lg font-medium transition-colors"
          >
            Close
          </button>
        </div>

      </div>
    </div>
  );
};
