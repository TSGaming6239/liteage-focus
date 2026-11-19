import React from 'react';
import { Search, X } from 'lucide-react';

interface SearchBarProps {
  query: string;
  onChange: (query: string) => void;
  resultCount: number;
}

export const SearchBar: React.FC<SearchBarProps> = ({ query, onChange, resultCount }) => {
  return (
    <div className="w-full max-w-2xl mx-auto">
      <div className="relative flex items-center shadow-sm">
        <div className="absolute left-4 pointer-events-none text-slate-400">
          <Search className="w-5 h-5" />
        </div>
        
        <input
          type="text"
          value={query}
          onChange={(e) => onChange(e.target.value)}
          placeholder="What are you struggling with? (e.g. distractions, time, notes, formulas...)"
          className="w-full pl-12 pr-24 py-3.5 sm:py-4 bg-white border border-slate-300 rounded-2xl text-slate-900 placeholder-slate-400 text-sm sm:text-base focus:outline-none focus:ring-2 focus:ring-blue-500/20 focus:border-blue-600 transition-all shadow-sm"
        />

        {query && (
          <button
            onClick={() => onChange('')}
            className="absolute right-14 text-slate-400 hover:text-slate-600 p-1.5 rounded-lg hover:bg-slate-100 transition-colors"
            title="Clear search"
          >
            <X className="w-4 h-4" />
          </button>
        )}

        <div className="absolute right-3.5 hidden sm:flex items-center text-xs font-medium text-slate-400 bg-slate-100 px-2.5 py-1 rounded-lg">
          {resultCount} {resultCount === 1 ? 'result' : 'results'}
        </div>
      </div>
    </div>
  );
};
