import React from 'react';
import { Platform } from '../types';
import { Monitor, Smartphone, Globe } from 'lucide-react';

interface Props {
  platform: Platform;
  size?: 'sm' | 'md';
}

export const CompatibilityBadge: React.FC<Props> = ({ platform, size = 'sm' }) => {
  const getIcon = () => {
    switch (platform) {
      case 'Windows':
      case 'macOS':
      case 'Linux':
        return <Monitor className={size === 'sm' ? 'w-3 h-3' : 'w-4 h-4'} />;
      case 'Android':
      case 'iOS':
        return <Smartphone className={size === 'sm' ? 'w-3 h-3' : 'w-4 h-4'} />;
      case 'Chrome / Edge Extension':
      case 'Web':
      default:
        return <Globe className={size === 'sm' ? 'w-3 h-3' : 'w-4 h-4'} />;
    }
  };

  return (
    <span className={`inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full font-medium bg-slate-100 text-slate-700 border border-slate-200 ${size === 'md' ? 'text-xs' : 'text-[11px]'}`}>
      {getIcon()}
      {platform}
    </span>
  );
};
