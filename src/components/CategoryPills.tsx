import React from 'react';
import { Category } from '../types';
import { CATEGORIES } from '../data/problemsData';
import { Compass, ShieldAlert, Clock, BookOpen, Brain, Award } from 'lucide-react';

interface CategoryPillsProps {
  selectedCategory: Category;
  onSelectCategory: (category: Category) => void;
}

export const CategoryPills: React.FC<CategoryPillsProps> = ({
  selectedCategory,
  onSelectCategory,
}) => {
  const getCategoryIcon = (category: Category) => {
    switch (category) {
      case 'Distractions':
        return <ShieldAlert className="w-4 h-4" />;
      case 'Time Management':
        return <Clock className="w-4 h-4" />;
      case 'Notes & Material':
        return <BookOpen className="w-4 h-4" />;
      case 'Revision & Memory':
        return <Brain className="w-4 h-4" />;
      case 'Exam Preparation':
        return <Award className="w-4 h-4" />;
      case 'All':
      default:
        return <Compass className="w-4 h-4" />;
    }
  };

  return (
    <div className="w-full">
      <div className="flex items-center gap-2 overflow-x-auto pb-2 scrollbar-none sm:flex-wrap sm:justify-center">
        {CATEGORIES.map((cat) => {
          const isSelected = selectedCategory === cat.value;
          return (
            <button
              key={cat.value}
              onClick={() => {
                // If already selected, toggle back to All (except for 'All' itself)
                if (isSelected && cat.value !== 'All') {
                  onSelectCategory('All');
                } else {
                  onSelectCategory(cat.value);
                }
              }}
              className={`flex items-center gap-2 px-4 py-2.5 rounded-xl text-xs sm:text-sm font-medium whitespace-nowrap transition-all border ${
                isSelected
                  ? 'bg-blue-600 text-white border-blue-600 shadow-sm shadow-blue-500/25 ring-2 ring-blue-600/20'
                  : 'bg-white text-slate-700 border-slate-200 hover:bg-slate-50 hover:border-slate-300'
              }`}
              title={isSelected && cat.value !== 'All' ? 'Click to deselect' : ''}
            >
              <span className={isSelected ? 'text-white' : 'text-slate-500'}>
                {getCategoryIcon(cat.value)}
              </span>
              <span>{cat.label}</span>
            </button>
          );
        })}
      </div>
    </div>
  );
};
